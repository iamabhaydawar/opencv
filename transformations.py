import cv2 as cv
import numpy as np

img=cv.imread('photos/tony1.jpeg')  

# cv.imshow('Original Image', img)


def translate(img, x, y):
    """
    Translate the image by x and y pixels.
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> left
# -y --> up
# x --> right
# y --> down
# translated = translate(img, -100, -100)
# cv.imshow('Translated Image', translated)

#rotation
def rotate(img,angle,rotPoint=None):
    (h,w)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(w//2,h//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(w,h)
    return cv.warpAffine(img,rotMat,dimensions)
rotated = rotate(img, -45)
# cv.imshow('Rotated Image', rotated)

rotated_rotated= rotate(img, -90)
# cv.imshow('Rotated Back Image', rotated_rotated)


#Resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized Image', resized)

#Flipping
flip = cv.flip(img, 0)  # 0 for vertical flip, 1 for horizontal flip, -1 for both
cv.imshow('Flipped Image', flip)

#Cropping
cropped=flip[100:400, 200:500]  # y1:y2, x1:x2
cv.imshow('Cropped Image', cropped)




cv.waitKey(0)