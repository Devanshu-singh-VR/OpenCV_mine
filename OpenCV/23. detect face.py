import cv2

face_cas = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()

    face = face_cas.detectMultiScale(img,1.1,4)
    if face == ():
        continue
    
    x,y,w,h = face[0]
    
    cv2.rectangle(img,(x,y),(x+w,y+h),(43,255,25),2)
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
    if k == ord('s'):
        break
