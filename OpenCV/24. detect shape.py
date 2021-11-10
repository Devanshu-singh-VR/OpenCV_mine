import cv2 as cv
import numpy as np

img = cv.imread('shape.png',1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thresh = cv.threshold(gray,240,255,cv.THRESH_BINARY)
contour,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

for count in contour:
    approx = cv.approxPolyDP(count, 0.01*cv.arcLength(count, True), True) #this function approx or heilight the polygon curve with precision(clearity)
    cv.drawContours(img,[approx], 0, (255,255,255),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx)==3: #contour length
        cv.putText(img,"Triangle",(x,y),cv.FONT_HERSHEY_PLAIN,1,(255,255,255))
    elif len(approx)==4: #contour length
        x,y,w,h = cv.boundingRect(approx)
        aspect_ratio = w/h
        if aspect_ratio>=0.95 and aspect_ratio<=1.05:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255))
        else:
            cv.putText(img,"Rectangle",(x,y),cv.FONT_HERSHEY_PLAIN,1,(255,255,255))
    elif len(approx)==5: #contour length
        cv.putText(img,"Pentagon",(x,y),cv.FONT_HERSHEY_PLAIN,1,(255,255,255))
    elif len(approx)==6: #contour length
        cv.putText(img,"Hexagon",(x,y),cv.FONT_HERSHEY_PLAIN,1,(255,255,255))
    elif en(approx)==10: #contour length
        cv.putText(img,"Star",(x,y),cv.FONT_HERSHEY_PLAIN,1,(255,255,255))
    else :
        cv.putText(img,"Circle",(x,y),cv.FONT_HERSHEY_PLAIN,1,(255,255,255))

cv.imshow('shapes',img)
cv.waitKey(0)