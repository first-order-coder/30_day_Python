import numpy as np
import cv2

capture = cv2.VideoCapture(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\Costa x BigDoggy x MasterD .mp4')

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    ''' The only color which will be shown is in the range of lower_blue and upper_blue others will get ignored'''

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Frame', result)

    if cv2.waitKey(37) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()