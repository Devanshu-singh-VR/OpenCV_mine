import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('D:\good.avi',fourcc, 20.0,(640,480) ) # save video at (20 frame per sec) and pixel size (640,480)

while True:
    rat,frame = cap.read() # capture the frame {rat for capturing image true or false}

    if rat == True:
        out.write(frame) # save the frame getting

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # conver frame to gray
        cv2.imshow('frame', gray)# show camera

        k = cv2.waitKey(1) # let a frame for 0.001 sec
        if k == ord('s') :
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()