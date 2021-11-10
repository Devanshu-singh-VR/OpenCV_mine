import cv2
img = cv2.imread('maa.png',1)

cv2.imshow('image',img)
cv2.waitKey(5000) # wait for image to load (5000) is 5 sec for image to show

cv2.imwrite('new.jpg',img) # save an image
