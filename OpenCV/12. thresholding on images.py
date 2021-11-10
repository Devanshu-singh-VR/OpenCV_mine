import cv2

cap = cv2.VideoCapture(0)

while True:
    read,frame = cap.read()

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _,img1 = cv2.threshold(img,160,255,cv2.THRESH_BINARY) # 122 is threshold value for all the pixels in the image (binary conversion)
    _,img2 = cv2.threshold(img,90,255,cv2.THRESH_TRUNC) # more many thresholds

    cv2.imshow('real',img)
    cv2.imshow('image',img1)
    cv2.imshow('image2',img2)

    k = cv2.waitKey(1)
    if k == ord('s'):
        break