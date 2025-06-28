import os
import cv2 as cv
import numpy as np

# Get the absolute path to the photos directory
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(os.path.dirname(current_dir), 'photos')

# List to store features and labels
features = []
labels = []

def create_train():
    # Group files by person (assuming filenames like tony1.jpg, tony2.jpg belong to same person)
    person_files = {}
    for file_name in os.listdir(path):
        # Get the person name from the file (e.g., 'tony' from 'tony1.jpg')
        person_name = ''.join([i for i in file_name if not i.isdigit()]).split('.')[0]
        if person_name not in person_files:
            person_files[person_name] = []
        person_files[person_name].append(file_name)
    
    # Print what we found
    print("Found the following people:")
    for person, files in person_files.items():
        print(f"{person}: {len(files)} images")
    
    # Process each person's images
    for person_id, (person_name, files) in enumerate(person_files.items()):
        print(f"\nProcessing {person_name}'s images...")
        for file_name in files:
            img_path = os.path.join(path, file_name)
            if os.path.isfile(img_path):
                image = cv.imread(img_path)
                if image is not None:
                    print(f"Processing {file_name}...")
                    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                    haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
                    rect_faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

                    if len(rect_faces) > 0:
                        for (x,y,w,h) in rect_faces:
                            face_roi = gray[y:y+h, x:x+w]
                            # Resize to consistent size
                            face_roi = cv.resize(face_roi, (150, 150))
                            features.append(face_roi)
                            labels.append(person_id)
                        print(f"Found {len(rect_faces)} face(s) in {file_name}")
                    else:
                        print(f"No faces found in {file_name}")

create_train()

if len(features) == 0:
    print("No faces were detected! Cannot train the model.")
    exit()

print(f'\nTraining completed:')
print(f'Total faces detected: {len(features)}')
print(f'Total labels assigned: {len(labels)}')

# Convert to numpy arrays with correct dtypes
features = np.array(features, dtype='float32')
labels = np.array(labels, dtype='int32')

# Train the recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

# Save the model and data
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

print("Model and data saved successfully!")