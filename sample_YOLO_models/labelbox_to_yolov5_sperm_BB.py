from labelbox import Client
import os
import cv2
import json
import argparse
import urllib.request
from collections import defaultdict

PROJECT_ID = "ckylnseaw8jtl0z9ig6pq03w3"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3NlbmM2eTYyMW9rMHlhNWRmdTRlaDZmIiwib3JnYW5pemF0aW9uSWQiOiJja3h6d2J4ajE2cWg1MHozbmQ3dmUyZ2E5IiwiYXBpS2V5SWQiOiJjbDljZjRvcGQyZWlsMDh5NmR4djQxcmk1Iiwic2VjcmV0IjoiYzgzMTUxMGU5NDg5OWJkMGE3YWI4YjYxMGU4ZTg0ZDgiLCJpYXQiOjE2NjU5ODk0OTQsImV4cCI6MjI5NzE0MTQ5NH0.uKZUeiDV2Y94w3QOXQJoJHhspHFwPiumT6e2_FtCsBg"
ENDPOINT = "https://api.labelbox.com/graphql"

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project-id", type=str, default=PROJECT_ID)
parser.add_argument("-a", "--api-key", type=str, default=API_KEY)
parser.add_argument("-o", "--output-dir", type=str, default="/work/vajira/DATA/VISEM-BB/new_download_2022_09_17_with_incomplete_test_data")

CLASS_ID_MAPPING = {}

def labelbox_to_yolov5(project_id, api_key, output_dir):

    client = Client(api_key=api_key, endpoint=ENDPOINT)
    project = client.get_project(project_id)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for label_object in project.video_label_generator():

        label_object = json.loads(label_object.json())

        video_name, video_ext = os.path.splitext(label_object["data"]["external_id"])
        video_url = label_object["data"]["url"]
        
        video_label_output_path = os.path.join(output_dir, video_name, "labels")
        video_frame_output_path = os.path.join(output_dir, video_name, "images")
        video_file_output_path = os.path.join(output_dir, video_name, "%s%s" % (video_name, video_ext))
        
        if not os.path.exists(video_label_output_path):
            os.makedirs(video_label_output_path)
            
        if not os.path.exists(video_frame_output_path):
            os.makedirs(video_frame_output_path)
        
        urllib.request.urlretrieve(video_url, video_file_output_path) 

        video_labels = defaultdict(list)

        video = cv2.VideoCapture(video_file_output_path)

        video_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        video_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

        frame_index = 0
        while(video.isOpened()):
            ret, frame = video.read()
            if ret == False:
                break
            cv2.imwrite(os.path.join(video_frame_output_path, "%s_frame_%i.jpg" % (video_name, frame_index)), frame)
            frame_index += 1
        video.release()

        for label in label_object["annotations"]:

            frame_id = label["frame"]
            class_name = label["name"]

            if class_name == "Zona pellucida (ZP) thickness":
                continue
            
            if class_name not in CLASS_ID_MAPPING:
                CLASS_ID_MAPPING[class_name] = len(CLASS_ID_MAPPING)

            class_id = CLASS_ID_MAPPING[class_name]
            
            start_x  = label["value"]["start"]["x"]
            start_y = label["value"]["start"]["y"]
            end_x = label["value"]["end"]["x"]
            end_y = label["value"]["end"]["y"]

            center_x =  (start_x + end_x) / 2
            center_y = (start_y + end_y) / 2
            label_width = end_x - start_x
            label_height = end_y - start_y

            norm_center_x = center_x / video_width
            norm_center_y = center_y / video_height
            norm_label_width = label_width / video_width
            norm_label_height = label_height / video_height

            video_labels[frame_id].append([class_id, norm_center_x, norm_center_y, norm_label_width, norm_label_height])

        image_path_file = open(os.path.join(output_dir, video_name, "%s.txt" % video_name), "w")
        for frame_index, frame_labels in video_labels.items():
            frame_save_path = os.path.join(video_label_output_path, "%s_frame_%i.txt" % (video_name, frame_index-1))
            image_path_file.write(frame_save_path + "\n")
            with open(frame_save_path, "w") as f:
                for frame_label in frame_labels:
                    f.write(" ".join([str(val) for val in frame_label]) + "\n")
        image_path_file.close()
        
    print("=== DONE ===")
    print("Class Label Mapping")
    for class_name, class_id in CLASS_ID_MAPPING.items():
        print("%s: %i" % (class_name, class_id))

    

if __name__ == "__main__":

    args = parser.parse_args()

    project_id = args.project_id
    api_key = args.api_key
    output_dir = args.output_dir

    labelbox_to_yolov5(project_id, api_key, output_dir)


