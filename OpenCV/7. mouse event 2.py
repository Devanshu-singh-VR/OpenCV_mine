import cv2
import numpy as np

def mouse(event,x,y,flag,pram):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),3,(0,0,300),-1)
        collect.append((x,y))
        if len(collect)>=2:
            cv2.line(img,collect[-1],collect[-2],(200,0,0),1)
        cv2.imshow('image',img)


collect = []
img = np.zeros((512,512,3))
cv2.imshow('image',img)

cv2.setMouseCallback('image',mouse)
cv2.waitKey(0)