import cv2
import numpy as np
import os


p = []
for person_name in os.listdir(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\train'):
    p.append(person_name)

haar_cascade = cv2.CascadeClassifier(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\haar_face.xml')

features = []
labels = []

people = p
DIR = r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\train'

for person in people:
    path = os.path.join(DIR, person)
    label = people.index[person]

    for img in os.listdir(path):
        img_path = os.path.join(path, img)

        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces_rect:
            face_roi = gray[y:y+h, x:x+w]
            features.append(face_roi)
            labels.append(label)



