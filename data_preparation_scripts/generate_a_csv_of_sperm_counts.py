import os
from natsort import natsorted


data_dir = "/work/vajira/DATA/VISEM-Tracking-from_kaggle/VISEM_Tracking_Train_v4/Train"

video_ids = os.listdir(data_dir)

with open("sperm_counts_per_frame.csv", "w") as f:

    f.write("frame_name, sperm_count, cluster_count, small_or_pinhead_count\n")

    for vid in video_ids:

        txt_files_path = os.path.join(data_dir, vid)
        txt_files = os.listdir(os.path.join(txt_files_path, "labels"))

        txt_files = natsorted(txt_files)

        for txt_file in txt_files:

            txt_path = os.path.join(txt_files_path,"labels", txt_file)
            #print(txt_path)

            with open(txt_path, "r") as tf:
                txt_lines = tf.readlines()

                sperm_count = 0
                cluster_count = 0
                small_or_pinhead_count = 0

                for txt_line in txt_lines:
                    #print(txt_line)
                    if int(txt_line[0])==0:
                        sperm_count+=1
                    elif int(txt_line[0])==1:
                        cluster_count+=1
                    elif int(txt_line[0])==2:
                        small_or_pinhead_count+=1

            frame_name= txt_file.split(".")[0]

            f.write(f"{frame_name},{sperm_count},{cluster_count},{small_or_pinhead_count}\n")    
            tf.close()
            print(int(txt_lines[-1][0]))

                #exit()






    


