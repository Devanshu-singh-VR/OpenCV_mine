import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('lena.png',1)
hist = cv2.calcHist([img],[1],None,[256],[0,256]) #img, (0b,1g,2r), bin .........
plt.plot(hist)
plt.show()
b,g,r = cv2.split(img)

plt.hist(b.ravel(),256,[0,255])# x , no of bars, range of x
plt.hist(g.ravel(),256,[0,255])
plt.hist(r.ravel(),256,[0,255])
plt.show()

cv2.waitKey(0)

