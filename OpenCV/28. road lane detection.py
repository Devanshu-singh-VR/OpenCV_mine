import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def region_of_interest(image,vertices):
    mask = np.zeros_like(image)
    # channel = image.shape[2]
    mask_color = 255
    cv.fillPoly(mask,vertices,mask_color)
    frame = cv.bitwise_and(image,mask)
    return frame

img = cv.imread('road.png')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

height = img.shape[0]
width = img.shape[1]

roi = [(0,height),(width/2,height/2),(width,height)]
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
canny = cv.Canny(gray,100,200,apertureSize=3)

imgg = region_of_interest(canny,np.array([roi],np.int32))

lines = cv.HoughLinesP(imgg,1,np.pi/180,80,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),5)

plt.imshow(img)
plt.show()