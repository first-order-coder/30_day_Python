import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\crowd-1584115_1920-1030x687.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(img_gray, 1.05, 3)
for (x,y,w,h) in face:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow('Face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()