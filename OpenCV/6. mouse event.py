import cv2
import numpy as np

def mouse(event,x,y,flag,pram):
    if event == cv2.EVENT_LBUTTONUP:
        XY = str(x)+" , "+str(y)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img,XY,(x,y),font,0.5,(255,255,255),1)
        cv2.imshow('image',img)
    elif event == cv2.EVENT_RBUTTONUP:
        blue = img[y,x,0] # y,x (0) is the index of blue color
        green = img[y,x,1] # same for both of them
        red = img[y,x,2] # or they are BGR channel for an image
        XY = str(blue) + " , " + str(green) +" , "+str(red)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, XY, (x, y), font, 0.5, (200, 400, 0), 1)
        cv2.imshow('image', img)

img = cv2.imread('D:\sec.jfif',1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',mouse) # inbuild function play the mouse event

cv2.waitKey(0)
