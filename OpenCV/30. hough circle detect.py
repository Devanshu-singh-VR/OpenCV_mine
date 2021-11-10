import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('color.png')
output = img.copy()
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.medianBlur(img,5)
circle = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=60,param2=30,minRadius=0,maxRadius=100)
detect = np.uint16(np.around(circle)) #use to round off the values of the matrix(number of circle,3)

for (x,y,r) in detect[0,:]:
    cv.circle(output,(x,y),r,(232,255,45),3)
    cv.circle(output, (x, y), 2, (120, 255,100), 3)


cv.imshow('image',output)
cv.waitKey(0)