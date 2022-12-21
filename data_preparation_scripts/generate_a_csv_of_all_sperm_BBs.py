import os
from natsort import natsorted
from tqdm import tqdm


data_dir = "/work/vajira/DATA/VISEM-Tracking-from_kaggle/VISEM_Tracking_Train_v4/Train"

video_ids = os.listdir(data_dir)

with open("sperm_all_BBs.csv", "w") as f:

    f.write("frame_name fid class bb0 bb1 bb2 bb3\n")

    for vid in tqdm(video_ids):

        txt_files_path = os.path.join(data_dir, vid)
        txt_files = os.listdir(os.path.join(txt_files_path, "labels_ftid"))

        txt_files = natsorted(txt_files)

        for txt_file in txt_files:

            txt_path = os.path.join(txt_files_path,"labels_ftid", txt_file)
            #print(txt_path)

            with open(txt_path, "r") as tf:
                txt_lines = tf.readlines()

                frame_name= txt_file.split(".")[0]

                for txt_line in txt_lines:
                    f.write(f"{frame_name} {txt_line}")  
            tf.close()
            #print(int(txt_lines[-1][0]))

                #exit()






    


