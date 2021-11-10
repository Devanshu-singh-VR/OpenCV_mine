import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(3,3000) # ste height to 3000 (3 belongs to height)
cap.set(4,3000) # set weight to 3000 (4 belongs to width size)
print(cap.get(3)) # print height new
print(cap.get(4)) # print new width

while True:
    rat,frame = cap.read() # capture the frame {rat for capturing image true or false}

    font = cv2.FONT_HERSHEY_COMPLEX
    time = str(datetime.datetime.now())
    frame = cv2.putText(frame,time,(10,50),font,1,(23,0,0),2,cv2.LINE_AA)

    cv2.imshow('frame', frame)# show camera

    k = cv2.waitKey(1) # let a frame for 0.001 sec
    if k == ord('s') :
        break

cap.release()
cv2.destroyAllWindows()