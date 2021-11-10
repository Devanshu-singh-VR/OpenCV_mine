import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('color.png',0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

'''
MORPHOLIGICAL TANSFORMATION
'''

kernel = np.ones((2,2),np.uint8) # make 2,2 square block to cover black spot on balls
dilation = cv2.dilate(mask,kernel,iterations=2) # use to dilute black spot
erosion = cv2.erode(mask,kernel,iterations=2) # THis will erode the boundary of ball
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) # erosion followed by dilation
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) # dilation followed by erosion
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) # difference between dilation and erosion

frame = [img,mask,dilation,erosion,opening,closing,mg]
name = ['img','mask','dilation','erosion','opening','closing','mg']
for i in range(len(frame)):
    plt.subplot(2,4,i+1)
    plt.imshow(frame[i])
    plt.xticks([]),plt.yticks([])
    plt.title(name[i])
plt.show()
