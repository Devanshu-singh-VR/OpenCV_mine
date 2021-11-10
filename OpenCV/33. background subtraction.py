import cv2 as cv
import numpy as np

cap = cv.VideoCapture('pedi.mp4')
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    _,frame = cap.read()

    if frame is None:
        break
    shadow = fgbg.apply(frame)

    cv.imshow('image',shadow)

    k = cv.waitKey(10)
    if k==ord('s'):
        break
