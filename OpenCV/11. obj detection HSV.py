import cv2
import numpy as np
def nothing(x):
    pass
# cap = cv2.VideoCapture(0) # for video camera

cv2.namedWindow('image')
cv2.createTrackbar('lh','image',0,255,nothing)
cv2.createTrackbar('ls','image',0,255,nothing)
cv2.createTrackbar('lv','image',0,255,nothing)

cv2.createTrackbar('uh','image',0,255,nothing)
cv2.createTrackbar('us','image',0,255,nothing)
cv2.createTrackbar('uv','image',0,255,nothing)

while True:
    # _,img = cap.read() # for video camera
    img = cv2.imread('color.png')

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # convert RBG image to HSV image

    lh = cv2.getTrackbarPos('lh','image')
    ls = cv2.getTrackbarPos('ls', 'image')
    lv = cv2.getTrackbarPos('lv', 'image')

    uh = cv2.getTrackbarPos('uh','image')
    us = cv2.getTrackbarPos('us', 'image')
    uv = cv2.getTrackbarPos('uv', 'image')

    lb = np.array([lh,ls,lv]) # upper and lower range for a color (HSV) not (RGB)
    ub = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lb,ub) # make an image between lb and ub

    frame = cv2.bitwise_and(img,img,mask=mask) # put a mask on image to purify it into wanted color

    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)


    k = cv2.waitKey(1)
    if k == 27:
        break

