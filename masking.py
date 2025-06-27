import cv2 as cv
import numpy as np


img=cv.imread('photos/tony2.jpeg')
cv.imshow('Original Image', img)

blank=np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)


mask = cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

mask2 = cv.rectangle(blank, 
                    (img.shape[1]//2, img.shape[0]//2),          # pt1 (x1,y1)
                    (img.shape[0]//2 + 100, img.shape[0]//2 + 100), # pt2 (x2,y2)
                    255,  # color
                    -1)   # thickness
cv.imshow('Mask2', mask2)

masked=cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)


cv.waitKey(0)