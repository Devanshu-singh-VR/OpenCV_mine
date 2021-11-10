import cv2
import numpy as np

img = cv2.imread('sudoku.jfif',0)
_,img1 = cv2.threshold(img,122,255,cv2.THRESH_BINARY)
img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,7)
img3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,7)

#cv2.imshow("image",img1)
cv2.imshow('adp',img2)
cv2.imshow('gauss',img3)

cv2.waitKey(0)
