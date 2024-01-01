import numpy as np
import cv2

capture = cv2.VideoCapture(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\emi.mp4')

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))
    print(frame.shape)
    # image = np.zeros(frame.shape, np.uint8)
    # smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    # image[:height//2, :width//2] = smaller_frame
    # image[height//2:, :width//2] = smaller_frame
    # image[:height//2, width//2:] = smaller_frame
    # image[height//2:, width//2:] = smaller_frame

    # cv2.imshow('new', image)

    if cv2.waitKey(34) == ord('q'):
        break
 
capture.release()
cv2.destroyAllWindows()