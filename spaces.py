import cv2 as cv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



img=cv.imread('photos/tony2.jpeg')
# cv.imshow('Original Image', img)

# img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(img_rgb)
# plt.show()

# #BGR to Grayscale conversion
# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

# #BGR to HSV conversion
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSV Image', hsv)

# #BGR to LAB conversion
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB Image', lab)


# #HsV to BGR conversion
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV to BGR Image', hsv_bgr)

# #LAB to BGR conversion
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR Image', lab_bgr)
cv.waitKey(0)