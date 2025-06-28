import cv2 as cv
import numpy as np
img= cv.imread('photos/tony2.jpeg')
cv.imshow('Original Image', img)

blank= np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)
blue=cv.merge([b, blank, blank])
green=cv.merge([blank, g, blank])
red=cv.merge([blank, blank, r])

cv.imshow('Blue Channel', blue)
cv.imshow('Green Channel', green)
cv.imshow('Red Channel', red)


print(f'Image Shape: {img.shape}')
print(f'Blue Channel Shape: {b.shape}')
print(f'Green Channel Shape: {g.shape}')
print(f'Red Channel Shape: {r.shape}')


print(b.shape, g.shape, r.shape)
merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)