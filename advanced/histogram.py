import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img= cv.imread('photos/tony2.jpeg')
# cv.imshow('Original Image', img)


blank=np.zeros(img.shape[:2], dtype='uint8')

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

mask=cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked=cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked Gray Image', masked)


# #gray scale histogram
# gray_hist= cv.calcHist([gray], [0], mask, [256], [0, 256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

#Color histogram
colors=('b','g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.title('Color Histogram')
plt.show()

cv.waitKey(0)