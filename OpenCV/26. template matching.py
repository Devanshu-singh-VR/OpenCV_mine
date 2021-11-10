'''METHOD TO FIND THE TEMPLATE ON THE LARGE IMAGE'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('bird.jpg',0) #'''IMAGE'''
frame = img[345:678,266:466] #'''TEMPLATE'''

h,w = frame.shape
res = cv.matchTemplate(img,frame,cv.TM_CCOEFF_NORMED)
loc = np.where(res>=0.97) # around 0.8 there will be a point which is brightest point in the image (and it will give the coordinates of that (the upper left corner))

for pt in zip(*loc[::-1]): # ::-1 is use to reverse he values to get (x,y)
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)

cv.imshow('img',img)
cv.imshow('frame',frame)
cv.waitKey(0)