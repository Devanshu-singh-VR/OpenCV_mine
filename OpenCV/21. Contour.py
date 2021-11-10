import cv2
import numpy as np

img = cv2.imread('color.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,225,0)
contour,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print('Number of contour : ',len(contour))

cv2.drawContours(img,contour,-1,(0,225,0),thickness=3)
cv2.imshow('img gray',gray)
cv2.imshow('img cont',img)

cv2.waitKey(0)
