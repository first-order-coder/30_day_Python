import cv2
import numpy as np

image = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')
blank = np.zeros((image.shape), dtype='uint8')
img = cv2.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), 5)
# img = cv2.rectangle(blank, (blank.shape[1]//2+5, 0), (blank.shape[1], blank.shape[0]//2), (255,0,0), 5)
# img = cv2.rectangle(blank, (blank[blank.shape[1]//2:, blank.shape[0]//2:]), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), 10)
# print(blank.shape[1]//2, blank.shape[0]//2)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()