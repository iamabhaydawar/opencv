import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)

# #1.Paint the image a certain color
# blank[:] = 0,0,255 #BGR format 
# cv.imshow('red',blank)

# #2.Draw a rectangle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)  #thickness=cv.FILLED will fill the rectangle
# # cv.imshow('rectangle',blank)


# #3.Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1) 
# # cv.imshow('circle',blank)

# #4.Draw a line
# cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
# cv.imshow('line',blank)


#5.Write text on image
cv.putText(blank,"Hello my name is abhay",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('text',blank)


cv.waitKey(0)

