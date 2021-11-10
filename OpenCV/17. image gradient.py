'''
image gradient is directional change in intensity and color of an image generally use as (edge detector)
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('njr.jpg',0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3) # img , datatype float, kernel size
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3) # another type of gradient
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobel_combine = cv2.bitwise_or(sobelx,sobely)

image = [img,lap,sobelx,sobely,sobel_combine]
name = ['image','lap','sobelx','sobely','sobel_comb']

for i in range(len(image)):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i])
    plt.xticks([]),plt.yticks([])
    plt.title(name[i])
plt.show()
