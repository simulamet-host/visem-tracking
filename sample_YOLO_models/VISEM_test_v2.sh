

# exp59: yolov5x.pt
model="yolo5x"
exp="exp59"
python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/52/images/52_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_52_frame_0" 


python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/54/images/54_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_54_frame_0" 

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/60/images/60_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_60_frame_0"

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/82/images/82_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_82_frame_0"  


# exp58: yolov5l.pt
model="yolo5l"
exp="exp58"
python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/52/images/52_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_52_frame_0" 


python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/54/images/54_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_54_frame_0" 

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/60/images/60_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_60_frame_0"

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/82/images/82_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_82_frame_0"  




# exp57: yolov5m.pt
model="yolo5m"
exp="exp57"
python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/52/images/52_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_52_frame_0" 


python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/54/images/54_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_54_frame_0" 

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/60/images/60_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_60_frame_0"

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/82/images/82_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_82_frame_0"  




exit 0
# exp56: yolov5s.pt
model="yolo5s"
exp="exp56"
python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/52/images/52_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_52_frame_0" 


python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/54/images/54_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_54_frame_0" 

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/60/images/60_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_60_frame_0"

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/82/images/82_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/${exp}/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "${exp}_${model}_final_82_frame_0"  
                    





# exp55: yolov5n.pt

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/52/images/52_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/exp55/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "exp55_yolo5n_final_52_frame_0" 


python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/54/images/54_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/exp55/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "exp55_yolo5n_final_54_frame_0" 

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/60/images/60_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/exp55/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "exp55_yolo5n_final_60_frame_0"

python detect.py    --img 640 \
                    --source /work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/82/images/82_frame_0.jpg \
                    --weights /work/vajira/DL/yolov5/runs/train/exp55/weights/best.pt \
                    --hide-conf --hide-labels --save-txt --save-conf \
                    --device 0 \
                    --project /work/vajira/DL/yolov5/runs/detect_VISEM_tracking \
                    --name "exp55_yolo5n_final_82_frame_0"  

