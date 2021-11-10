import cv2
import numpy as np

img = np.zeros((250,500,3),np.uint8)
img2 = np.zeros((250,500,3),np.uint8)
img = cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.rectangle(img2,(250,0),(500,250),(255,255,255),-1)

cv2.imshow('kk',img2)
cv2.imshow("image",img)
bitw = cv2.bitwise_xor(img,img2) # or ,and ,not or etc.......

cv2.imshow("show",bitw)
cv2.waitKey(0)
