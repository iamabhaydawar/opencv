import cv2 as cv
import numpy as np

img=cv.imread('photos/tony2.jpeg')
# cv.imshow('Original Image', img)

blank = np.zeros(img.shape,dtype='uint8')
# cv.imshow('Blank Image', blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blurred Image', blur)

canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges', canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Thresholded Image', thresh)

countours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Number of contours found: {len(countours)}')

cv.drawContours(blank,countours,-1,(0,0,255),thickness=2)
cv.imshow('Contours', blank)

cv.waitKey(0)