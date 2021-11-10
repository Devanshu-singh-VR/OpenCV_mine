import cv2 as cv
import numpy as np

def printer(x):
    print(x)

img = np.zeros((255,255,3),np.uint8)

cv.namedWindow('image') # update a new permanent window

cv.createTrackbar('B','image',0,255,printer)  # creat trackbar
cv.createTrackbar('G','image',0,255,printer)
cv.createTrackbar('R','image',0,255,printer)

switch = 'ON-OFF'
cv.createTrackbar(switch,'image',0,1,printer)

while True:
    cv.imshow('image',img)
    k = cv.waitKey(1)
    if k==27:
        break

    B = cv.getTrackbarPos('B','image') # get the value of B unit
    G = cv.getTrackbarPos('G', 'image')
    R = cv.getTrackbarPos('R', 'image')
    S = cv.getTrackbarPos(switch,'image')

    if S==0:
        img[:] = [0,0,0]
    else:
        img[:] = [B,G,R]

