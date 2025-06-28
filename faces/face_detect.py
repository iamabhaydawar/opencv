import cv2 as cv
import numpy as np
import os

img = cv.imread('photos/pokercats.jpeg')
# cv.imshow('Original Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

# Use extended cat face cascade for better detection
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalcatface_extended.xml')
rect_faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=3, minSize=(60, 60), maxSize=(150, 150))

print(f'Number of cat faces detected: {len(rect_faces)}')

for (x,y,w,h) in rect_faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow('Detected Cat Faces', img)

cv.waitKey(0)

