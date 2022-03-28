from sys import path
path.append(r"C:\Users\ahmad\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages")
import numpy as np
import cv2 as cv

capture = cv.VideoCapture(0)

while True:    # USED TO READ FRAME BY FRAME
    isTrue, frame = capture.read()   # READ RETURNS THE FRAME AND A A BOOLEAN IF IT WAS READ
    gray_face = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(frame, 1.1, 9, None)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    cv.imshow('Video', frame)        # DISPLAY INDVIDUAL FRAMES
    if cv.waitKey(20) and 0xFF == ord('d'):
        break
capture.release()
