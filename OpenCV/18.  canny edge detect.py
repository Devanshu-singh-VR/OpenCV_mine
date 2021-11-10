import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('landmark.png',0)

canny = cv2.Canny(img,100,255)

cv2.imshow('Canny',canny)
cv2.waitKey(0)
