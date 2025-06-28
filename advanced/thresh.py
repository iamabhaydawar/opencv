import cv2 as cv


img = cv.imread('photos/tony2.jpeg')
cv.imshow('Original Image', img)


#Simple Thresholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold', thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 45, 3)
cv.imshow('Adaptive Threshold', adaptive_thresh)

cv.waitKey(0)