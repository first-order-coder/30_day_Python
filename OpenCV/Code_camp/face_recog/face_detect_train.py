import numpy as np
import cv2
import os

p = []
for i in os.listdir(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\train'):
    p.append(i)

people = p
DIR = r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\train'

haar_cascade = cv2.CascadeClassifier(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)


create_train()
print('-------------- Training Done ---------------')

features = np.array(features, dtype= 'object')
labels = np.array(labels)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)



