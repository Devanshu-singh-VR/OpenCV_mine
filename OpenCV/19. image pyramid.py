import cv2
import numpy as np

img = cv2.imread('boi.jfif')
pr1 = cv2.pyrDown(img)# blurr and decrease the resolution of an image
pr2 = cv2.pyrDown(pr1) # cv also has pyrUp

cv2.imshow('img',img)
cv2.imshow('pr1',pr1)
cv2.imshow('pr2',pr2)

cv2.waitKey(0)

