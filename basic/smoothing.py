import cv2 as cv

img=cv.imread('photos/tony2.jpeg')
cv.imshow('Original Image', img)

#Average Smoothing
average = cv.blur(img, (3, 3))
cv.imshow('Average Smoothing', average)

#Gaussian Smoothing
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Smoothing', gaussian)

#Median Smoothing   
median = cv.medianBlur(img, 3)
cv.imshow('Median Smoothing', median)


#Bilateral Smoothing
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Smoothing', bilateral)

cv.waitKey(0)