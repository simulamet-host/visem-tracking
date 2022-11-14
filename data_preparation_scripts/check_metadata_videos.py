import os
import argparse
import cv2
import datetime


argparse = argparse.ArgumentParser()
argparse.add_argument("--input", help="Input video file",  required=True)
opt = argparse.parse_args()


cap = cv2.VideoCapture(opt.input)
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
 
# calculate duration of the video
seconds = round(frames / fps)
video_time = datetime.timedelta(seconds=seconds) 

print("Frames=", frames)
print("FPS=", fps)
print("seconds=", seconds)
print("video_time",  video_time)

#print(opt)