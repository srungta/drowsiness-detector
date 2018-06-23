import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('C:\\Users\\shrung\\AppData\\Local\\Continuum\\miniconda3\\envs\\deeplearning\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\\Users\\shrung\\AppData\\Local\\Continuum\\miniconda3\\envs\\deeplearning\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

video_capture = cv.VideoCapture(0)
import time
time.sleep(5)
while True:
    # capture video from feed.
    ret, img = video_capture.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv.imshow('img',img)
    # Wait for a key press event. In this case, wait for at least 30 ms for 'Space' key.
    k = cv.waitKey(30) & 0xFF
    if k == 32:
        break

cv.destroyAllWindows()
video_capture.release()