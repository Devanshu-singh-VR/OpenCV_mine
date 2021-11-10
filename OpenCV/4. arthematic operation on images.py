import cv2
import numpy as np

img = cv2.imread('maa.png',1)
img2 = cv2.imread("saa.png",1)

img = cv2.resize(img,(400,400)) # use to reshape the image
img2 = cv2.resize(img2,(400,400))

b,g,r = cv2.split(img) # split image to RGB

final = cv2.addWeighted(img,.5,img2,.5,0) # add images (alp , bita ,constant)
cv2.imshow("image",final)
print(img.shape)
cv2.waitKey(0)


