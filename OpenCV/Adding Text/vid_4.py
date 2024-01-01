import numpy as np
import cv2

capture = cv2.VideoCapture(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Vid_2\Costa x BigDoggy x MasterD .mp4')

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(frame, 'Ginura IS OG', (100, height - 10), font, 1, (0, 0, 255), 3, cv2.LINE_AA )

    cv2.imshow('Image', frame)

    if cv2.waitKey(37) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()