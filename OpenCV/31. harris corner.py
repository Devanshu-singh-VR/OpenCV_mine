import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

imgg = cv.imread('chess.jpg')

img = np.float32(cv.cvtColor(imgg,cv.COLOR_BGR2GRAY))

img = cv.cornerHarris(img,2,5,0.04)
img = cv.dilate(img,None)

imgg[img> 0.0000004*img.max()] = [0,255,0]

cv.imshow('chess',imgg)

cv.waitKey(0)
