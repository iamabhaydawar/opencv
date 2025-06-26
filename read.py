import sys
sys.path.append('/home/iamabhaydawar/.local/lib/python3.12/site-packages')
import cv2 as cv
import numpy as np

#reading images
# img1 = cv.imread('photos/tony1.jpeg')
# img2 = cv.imread('photos/tony2.jpeg')

# img1 = cv.resize(img1, (500, 500))
# img2 = cv.resize(img2, (500, 500))

# cv.imshow('tony1', img1)
# cv.imshow('tony2', img2)

cv.waitKey(0)

# #reading videos
# capture = cv.VideoCapture('videos/video1.mp4')
# while True:
#     isTrue,frame = capture.read()
#     cv.imshow('video',frame)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()