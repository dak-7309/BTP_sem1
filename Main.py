import cv2
import numpy as np
import argparse
import os
from utils import process_frame, draw_prediction
import time
import math
from datetime import date
import os
import sys
import shutil


CONF_THRESHOLD = 0.3
NMS_THRESHOLD = 0.4

with open('Model_Data/coco.names', 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

net = cv2.dnn.readNet(os.path.abspath("Model_Data/yolov4_tiny.weights"), os.path.abspath("Model_Data/yolov4_tiny.cfg"), "darknet")
outNames = net.getUnconnectedOutLayersNames()
writer = None

cap = cv2.VideoCapture('Data/walking.avi')
# cap = cv2.VideoCapture('Data/sd2.mp4')
# cap = cv2.VideoCapture('Data/violence.mp4')

count = 0
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS= ",fps)
v=fps//5+1

parent_dir=os.path.abspath(os.getcwd())
p = "Violation Frames"
p1 = os.path.join(parent_dir, p) 

try:  
    os.mkdir(p1)  
except OSError as error:  
    shutil.rmtree(p)
    os.mkdir(p1)


t0 = time.time()

while(cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        break;
    
    if(count%(v)==0):
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        outs = net.forward(outNames)
        L=process_frame(frame, outs, classes, CONF_THRESHOLD, NMS_THRESHOLD)
        
        # social distancing not followed
        if L>0:
            today = date.today()
            t = time.localtime()
            date_=today.strftime("%b-%d-%Y")
            current_time = time.strftime("%H:%M:%S", t)
            ttt=""
            for q in range(len(current_time)):
                if current_time[q]==":":
                    ttt+="-"
                else:
                    ttt+=current_time[q]
            
            img_name=p1+"/"+date_+"_"+ttt+"_"+str(L)+".png"
            cv2.imwrite(img_name, frame)  
            
        cv2.imshow("Output", frame)
        
        key=cv2.waitKey(5)
        
        if key==27:
            break

    count+=1

t1 = time.time()

cap.release()
# writer.release()
cv2.destroyAllWindows()

total = t1-t0
print("Total time taken= ",total)