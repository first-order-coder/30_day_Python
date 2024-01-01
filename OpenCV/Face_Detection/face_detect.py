import numpy as np
import cv2

capture = cv2.VideoCapture(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\emi.mp4')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True: #why we use while loop here is because we want the programme to keep capturing the feed
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6) #will give out the cordinates of the found faces

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+h, x:x+w] #region of interest
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 6)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ew, eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(30) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
        
    
