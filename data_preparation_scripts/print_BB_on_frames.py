import os
import torch
import torchvision
from torchvision.io import read_image # To read images
from torchvision.utils import draw_bounding_boxes # To show BBs
import matplotlib.pyplot as plt
import numpy as np



# To convert YOLO format to torch friedly format
def ccwh2xyxy(img_h, img_w, bb_box):
    norm_center_x = bb_box[0]
    norm_center_y = bb_box[1]
    norm_label_width = bb_box[2]
    norm_label_height = bb_box[3]
    
    center_x = norm_center_x * img_w
    center_y = norm_center_y * img_h
    label_width = norm_label_width * img_w
    label_height = norm_label_height * img_h
    
    x_min = center_x - (label_width/2)
    y_min = center_y - (label_height/2)
    x_max = center_x + (label_width/2)
    y_max = center_y + (label_height/2)
    
    return [x_min, y_min, x_max, y_max]


def get_bboex(bb_txt_path, img_h, img_w):
    
    bboxes = []
    classes = []
    with open(bb_txt_path, "r") as f:
        bbs = f.read().splitlines()
    
        for bb in bbs:
            crd = list(map(float, (bb.split())))
            cls_id  = int(crd[0])
            crd = ccwh2xyxy(img_h, img_w, crd[1:]) 
            bboxes.append(crd)
            classes.append(cls_id)
    
    return classes, bboxes

# Show the images
def save_images(img_path, bb_txt_path, save_path):
    
    #print(bb_txt_path)
    img = read_image(img_path)
    os.makedirs(save_path, exist_ok=True)
    
    file_name = img_path.split("/")[-1].split(".")[0]

    img_height = img.shape[1]
    img_width = img.shape[2]
    
    # draw bounding boxes
    # bounding box in (xmin, ymin, xmax, ymax) format
    #bbox1 = [30, 45, 330, 450]
    #bbox2 = [320, 150, 440, 460]
    classes, bbox = get_bboex(bb_txt_path, img_height, img_width)
    bbox = torch.tensor(bbox, dtype=torch.int)
    #print(bbox)
    #print(bbox.size())

    # draw bounding boxes on the input image
    img=draw_bounding_boxes(img, bbox, width=3,
    colors=[(255,0,0) if c==0 else (0,255,0) if c==1 else (0, 0, 255) for c in classes])
    img = torchvision.transforms.ToPILImage()(img)
    
    #img = torchvision.transforms.ToPILImage()(img)
    img = np.array(img)
    plt.imshow(img)
    plt.imsave("{}/{}.pdf".format(save_path, file_name), img)
    # print(classes)

if __name__=="__main__":

    test_ids = [52, 54, 60, 82]

    for id in test_ids:

        img_path = f"/work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/{id}/images/{id}_frame_0.jpg"
        bb_path =  f"/work/vajira/DATA/VISEM-BB/to_yolo5_05_08_2022_20_corrected_index_and_feature_ids/{id}/labels/{id}_frame_0.txt"

        save_path = "/work/vajira/DL/visem_tracking_simulamet_repo/visem-tracking/sample_images"

        save_images(img_path, bb_path, save_path)