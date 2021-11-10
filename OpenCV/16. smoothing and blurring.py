import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('s&p.jpeg') #also uee boi.jfif for filter to gauss blurr method

kernel = np.ones((5,5),np.float32)/25
filter = cv2.filter2D(img,-1,kernel) #by blurring the image it smooth the image (like it remove the noice from an image)
blur = cv2.blur(img,(5,5))
gauss = cv2.GaussianBlur(img,(5,5),0) # kernel is like converging to center (good one)
median = cv2.medianBlur(img,5) # kernel always of odd except 1 ( it replace each pixel value with its neighbour pixel) use for salt and pepper filter
bf = cv2.bilateralFilter(img,9,75,75) # filter and smooth edges

image = [img,filter,blur,gauss,median,bf]
name = ['image','filter','blur','gaussian','median','bilateral']
for i in range(len(image)):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i])
    plt.yticks([]),plt.xticks([])
    plt.title(name[i])
plt.show()