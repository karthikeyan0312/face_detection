import numpy as np
import cv2
import tensorflow
files=#place the haarcascade file location
fcascade=cv2.CascadeClassifier(files)
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret, img = cap.read()
    #frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=fcascade.detectMultiScale(gray,scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20))
    for (x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0, 0, 255),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]    
    #cv2.imshow('Color', img)
    cv2.imshow('Project', img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
