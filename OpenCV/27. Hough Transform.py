'''UES TO DETECT ANY SHAPE IF IT IS CONVERTED INTO MATHEMATIC FORMAT (DISTORTED OR NOICE)'''

import cv2 as cv
import numpy as np

img = cv.imread('road.png') #also use sudoku image
edge = cv.Canny(img,50,150,apertureSize=3)
cv.imshow('canny',edge)
lines = cv.HoughLinesP(edge,1,np.pi/180,80,minLineLength=100,maxLineGap=4)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv.imshow('image',img)
cv.waitKey(0)


