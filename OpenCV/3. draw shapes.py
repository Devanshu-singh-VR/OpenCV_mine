import cv2
import numpy as np

img = cv2.imread('maa.png',1)

img = cv2.line(img,(0,0) , (255,255) , (255,314,11), 10) # start coord , end coord , (B,G,R) , thickness
img = cv2.arrowedLine(img,(0,255) , (255,234) , (23,34,55), 10)
img = cv2.rectangle(img, (344,0),(444,555),(0,0,443),10)
img = cv2.circle(img , (447,63), 64,(344,0,0),-1) # center , radius
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"HELLO",(10,500),font,2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
