import cv2
import numpy as np

capture = cv2.VideoCapture('move.mp4')
ret,frame1 = capture.read()
ret,frame2 = capture.read()
frame2 = cv2.resize(frame2,(500,500))
frame1 = cv2.resize(frame1,(500,500))

while True:
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,20,225,cv2.THRESH_BINARY)
    dilute = cv2.dilate(thresh,None,iterations=3)
    contour,_ = cv2.findContours(dilute,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for coun in contour:
        x,y,w,h = cv2.boundingRect(coun)

        if cv2.contourArea(coun)<900:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),thickness=2)
        cv2.putText(frame1,'statue : moving',(7,10),cv2.FONT_HERSHEY_PLAIN,2,(0,21,34),thickness=1)

    #cv2.drawContours(frame1,contour,-1,(0,255,0),thickness=2)
    cv2.imshow('image',frame1)

    frame1 = frame2
    ret,frame2 = capture.read()
    frame2 = cv2.resize(frame2, (500, 500))

    k = cv2.waitKey(20)
    if k==ord('s'):
        break

