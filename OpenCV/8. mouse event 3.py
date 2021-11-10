import cv2
import numpy as np

def mouse(event,x,y,flag,pram):
    if event == cv2.EVENT_LBUTTONUP:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        new = np.zeros((540,540,3),np.uint8)
        new[:] = [blue,green,red] # convert every pixel unit into BGR format

        cv2.imshow('new',new)

img = cv2.imread('maa.png',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',mouse)
cv2.waitKey(0)
