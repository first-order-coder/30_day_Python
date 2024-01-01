import numpy as np
import cv2 as cv
import os

# haar_cascade = cv2.CascadeClassifier(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\face_recog\haar_face.xml')

# p = []
# for i in os.listdir(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\train'):
#     p.append(i)

# people = p

# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\face_recog\face_trained.yml')

# img_to_serach = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\val\ben_afflek\2.jpg')
# gray = cv2.cvtColor(img_to_serach, cv2.COLOR_BGR2GRAY)
# cv2.imshow('person', gray)

# faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
# for (x, y, w, h) in faces_rect:
#     face_roi = gray[y:y+h, x:x+w]

#     label, confidence = face_recognizer.predict(face_roi)
#     print(f'{people[label]} and {confidence}')

#     cv2.putText(img_to_serach, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
#     cv2.rectangle(img_to_serach, (x,y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow('Detected', img_to_serach)
# cv2.waitKey(0)


haar_cascade = cv.CascadeClassifier(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\face_recog\haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\face_recog\face_trained.yml')

img = cv.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Code_camp\Assestes\val\ben_afflek\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)