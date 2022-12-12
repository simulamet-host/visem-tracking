 
# Only using training data
 #python train.py --img 640 --batch 16 --epochs 300 --data VISEM_Tracking_fold_1.yaml --weights yolov5s.pt

# adding validation data to dataset (Exp 38)
#python train.py --img 640 --batch 2 --epochs 30 --data VISEM_Tracking_fold_1_with_more_test_data.yaml --weights yolov5n.pt 



#python train.py --img 640 --batch 16 --epochs 50 --data VISEM_Tracking_after_index_corrections.yaml --weights yolov5m.pt --device 0

# after correcting index problem (Exp 55)
python train.py --img 640 --batch 16 --epochs 50 --data VISEM_Tracking_after_index_corrections.yaml --weights yolov5n.pt --device 0


# after correcting index problem (Exp 56)
python train.py --img 640 --batch 16 --epochs 50 --data VISEM_Tracking_after_index_corrections.yaml --weights yolov5s.pt --device 0

# after correcting index problem (Exp 57)
python train.py --img 640 --batch 16 --epochs 50 --data VISEM_Tracking_after_index_corrections.yaml --weights yolov5m.pt --device 0

# after correcting index problem (Exp 58)
python train.py --img 640 --batch 16 --epochs 50 --data VISEM_Tracking_after_index_corrections.yaml --weights yolov5l.pt --device 0

#after correcting index problem (Exp 59)
python train.py --img 640 --batch 16 --epochs 50 --data VISEM_Tracking_after_index_corrections.yaml --weights yolov5x.pt --device 0



