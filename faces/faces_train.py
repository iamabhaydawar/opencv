import os
import cv2 as cv
import numpy as np

path = 'photos'
# images = []
# for i in os.listdir(path):
#     images.append(i)
# print(f'Number of images found: {len(images)}')

features = []
labels=[]
def create_train():
    for i, file_name in enumerate(os.listdir(path)):
        img_path = os.path.join(path, file_name)
        if os.path.isfile(img_path):
            image = cv.imread(img_path)
            if image is not None:
                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalcatface_extended.xml')
                rect_faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=3, minSize=(60, 60), maxSize=(150, 150))

                for (x,y,w,h) in rect_faces:
                    face_roi = gray[y:y+h, x:x+w]
                    features.append(face_roi)
                    labels.append(i)

create_train()
# print(f'Number of faces found: {len(features)}')
# print(f'Number of labels found: {len(labels)}')
print(f'Training completed')

features = np.array(features, dtype='object')
labels = np.array(labels)

#instantiate the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
#Train the recognizer on the features list and labels list
face_recognizer.train(features, labels)

np.save('features.npy', features)
np.save('labels.npy', labels)