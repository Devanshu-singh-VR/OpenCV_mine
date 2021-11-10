import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('saa.png',1)
img = cv2.resize(img,(600,480))

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #convert bgr to rgb format

cv2.imshow('image',img)
plt.imshow(img1) #matplotlib always show image into RGB format
plt.show()

cv2.waitKey(0)
