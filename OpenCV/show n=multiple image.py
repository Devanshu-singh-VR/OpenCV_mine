import matplotlib.pyplot as plt
import cv2

i1 = cv2.imread('maa.png',1)
i2 = cv2.imread('saa.png',1)
i3 = cv2.imread('color.png',1)
i4 = cv2.imread('sudoku.jfif',1)

img = [i1,i2,i3,i4]
name = ['maa','saa','color','sudoku']

for i in range(4):
    plt.subplot(2,2,i+1) # shape of frame(2,2) and count of image
    plt.xticks([]),plt.yticks([]) # remove the coordinates
    plt.imshow(img[i])
    plt.title(name[i])
plt.show()
