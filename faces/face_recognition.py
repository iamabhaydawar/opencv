import numpy as np
import cv2 as cv
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the trained face recognizer
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the features and labels from the correct path
features_path = os.path.join(current_dir, 'features.npy')
labels_path = os.path.join(current_dir, 'labels.npy')
features = np.load(features_path, allow_pickle=True)
labels = np.load(labels_path)

# Create and load the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_trained_path = os.path.join(current_dir, 'face_trained.yml')
face_recognizer.read(face_trained_path)

# Get people names from the photos directory
photos_dir = os.path.join(current_dir, '..', 'photos')
people = []
for file_name in os.listdir(photos_dir):
    person_name = ''.join([i for i in file_name if not i.isdigit()]).split('.')[0]
    if person_name not in people:
        people.append(person_name)
people.sort()  # Sort to ensure consistent ordering
print("People in the dataset:", people)

# Use one of the existing images in the photos directory
img_path = os.path.join(current_dir, '..', 'photos', 'tony2.jpeg')
img = cv.imread(img_path)
if img is None:
    print(f"Error: Could not load image from {img_path}")
    exit()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

if len(faces_rect) == 0:
    print("No faces detected in the image!")
    exit()

print(f"Found {len(faces_rect)} faces in the image")

for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h, x:x+w]
    # Resize to match training size
    face_roi = cv.resize(face_roi, (150, 150))
    
    label, confidence = face_recognizer.predict(face_roi)
    
    # Convert confidence to percentage (100% = perfect match)
    confidence_pct = 100 - confidence
    person_name = people[label] if 0 <= label < len(people) else "Unknown"
    
    print(f'Detected: {person_name} (Label {label}) with {confidence_pct:.2f}% confidence')

    # Draw the results
    cv.putText(img, f'{person_name} ({confidence_pct:.1f}%)', 
              (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)
cv.destroyAllWindows()

