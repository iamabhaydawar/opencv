import cv2 as cv
img = cv.imread('photos/tony1.jpeg')
img = cv.resize(img, (500, 500))

# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
# cv.imshow('tony1', img)

# #Blurring an image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# #Edge Cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges', canny)


#Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated', dilated)

#Eroding the image
eroded=cv.erode(dilated,(3,3),iterations=3)
cv.imshow('eroded', eroded)

#Resize and crop the image
resized = cv.resize(eroded, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)


# Cropping the image
crop = img[50:200, 200:400]  # y1:y2, x1:x2
cv.imshow('cropped', crop)

# Cropping the image
cv.waitKey(0)