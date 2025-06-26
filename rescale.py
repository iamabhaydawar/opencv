import sys
sys.path.append('/home/iamabhaydawar/.local/lib/python3.12/site-packages')
import cv2 as cv
img=cv.imread('photos/tony1.jpeg')
cv.imshow('tony1',img)

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('resized_image',resized_image)


#reading videos
capture = cv.VideoCapture('videos/video1.mp4')
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.5)
    
    # cv.imshow('video',frame)
    cv.imshow('video_resized',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()