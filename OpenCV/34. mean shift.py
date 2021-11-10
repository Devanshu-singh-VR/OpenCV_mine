import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture('pedestrian.mp4')
ret,frame = cap.read()

x,y,w,h = 1083,325,47,61
track = (x,y,w,h)

roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
hist_roi = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(hist_roi, hist_roi, 0, 255, cv.NORM_MINMAX)

term = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)

while True:
    ret,frame = cap.read()

    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], hist_roi, [0,180], 1)

        ret,track= cv.meanShift(dst, track, term)

        x,y,w,h = track
        cv.rectangle(frame, (x, y), (x+w, y+h), 255, 3)
        cv.imshow('img',frame)
        k = cv.waitKey(0)
        if k==ord('s'):
            break
    else:
        break
