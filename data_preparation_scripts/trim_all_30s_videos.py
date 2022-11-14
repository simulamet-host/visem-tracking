import subprocess
import os
from datetime import timedelta
#import ffmpeg


input_dir = "/home/vajira/data/VISEM_original/visem-dataset/videos"
output_dir = "/home/vajira/data/VISEM_original/visem-extracted-30s-including-first-30s"


CHUNK_SIZE = 30


os.makedirs(output_dir,exist_ok=True)

v_files = os.listdir(input_dir)


def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

for v_file in v_files:
    input_file = os.path.join(input_dir, v_file)
    v_file_id = v_file.split(".")[0].split("_")[0]
    print(v_file_id)

    total_time_s = get_length(input_file)
    print(total_time_s)
    time_30s_chunks = [t for t in range(0, int(total_time_s), CHUNK_SIZE)]

    #for t30 in time_30s_chunks:
    #    print(timedelta(seconds=t30))
#exit()

    for tt in time_30s_chunks[:-1]:
        
        trim_start= tt
        trim_stop = tt + CHUNK_SIZE
        
        output_path = os.path.join(output_dir, f'{v_file_id}_{trim_start}_{trim_stop}.mp4')
        trim_start_hh_mm_ss = str(timedelta(seconds=trim_start))
        trim_stop_hh_mm_ss = str(timedelta(seconds=trim_stop))
        chunk_size_hh_mm_ss = str(timedelta(seconds=CHUNK_SIZE))
        print("trim start=", trim_start_hh_mm_ss)
        print("trim stop=", trim_stop_hh_mm_ss)
        print("chunk size=", chunk_size_hh_mm_ss)
        cmd = f'ffmpeg -i {input_file} -ss {trim_start_hh_mm_ss} -t {chunk_size_hh_mm_ss} -c:v libx264 {output_path}'
        print("CMD RUNNING=", cmd)
        subprocess.run(str(cmd), shell=True)


    #ffmpeg -i videos/623.mkv -ss 00:00:00 -t 00:00:30 -c:v libx264 output3.mp4