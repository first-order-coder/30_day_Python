import numpy as np
import cv2

# a = np.array([
#     [[0, 1],
#      [2, 3]],
#      [[5, 6],
#       [7, 8]]
#     ])

# print(a.ravel())

capture = cv2.VideoCapture(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Vid_2\Costa x BigDoggy x MasterD .mp4')

while True:
    ret, frame = capture.read()
    height = int(capture.get(4))
    width = int(capture.get(3))

    # image = np.zeros(frame.shape, np.uint8)
    # smaller_frame = cv2.resize(frame, (0,0), fx=0.9, fy=0.9)

    img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10)
    img = cv2.rectangle(img, (100, 100), (400, 400), (128, 128, 128), 3) #-1 will fill in the rectangle
    img = cv2.circle(img, (250,250), 100, (0, 0, 255), 3)
    

    cv2.imshow('frame', frame) #first output is shown and then quitting is created

    if cv2.waitKey(38) == ord('q'):
        break
  
capture.release()
cv2.destroyAllWindows()
