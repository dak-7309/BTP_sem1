import cv2
import numpy as np
import math
from scipy.spatial import distance as dist

def draw_prediction(frame, classes, classId, conf, left, top, right, bottom,color,temp,L):

    if classes:
        assert(classId < len(classes))
    # if classes[classId]=='person':
    cv2.rectangle(frame, (left, top), (right, bottom), color,2)
    
    if temp==False:
        text="Number of Social Distancing Violations= "+str(L)
        cv2.putText(frame,text,(15,frame.shape[0]-15),cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 1)
        


def process_frame(frame, outs, classes, confThreshold, nmsThreshold):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height,center_x,center_y])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)

    violate=set()


    results=[]
    for i in indices:
        i = i[0]
        if classes[classIds[i]]=="person":
            box = boxes[i]
            x = box[0]
            y = box[1]
            width = box[2]
            height = box[3]
            centerx=int(x+width/2)
            centery=int(y+height/2)
            r=(i,(x,y,x+width,y+height),(centerx,centery))
            results.append(r)
        

    temp=False
    if len(results)>=2:

        c=np.array([r[2] for r in results ])
        d=dist.cdist(c, c, metric="euclidean")

        for i in range(d.shape[0]):
            for j in range(i+1,d.shape[1]):
                if d[i,j]<90:
                    violate.add(i)
                    violate.add(j)
        

        for (i,(ind,bbox,center)) in enumerate(results):
            (startx,starty,endx,endy)=bbox
            (cx,cy)=center
            color=(0,255,0)

            if i in violate:
                color=(0,0,255)
            draw_prediction(frame, classes, classIds[ind], confidences[ind], startx, starty, endx,endy,color,temp,len(violate))
            temp=True
    return len(violate)

    








