import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('mann.jpg')

img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corner = cv.goodFeaturesToTrack(img,1000,0.01,10)
corner = np.int0(corner)

for i in corner:
    x,y = i.ravel()
    cv.circle(img,(x,y),5,(122,0,255),-1)

cv.imshow('chess',img)

cv.waitKey(0)
