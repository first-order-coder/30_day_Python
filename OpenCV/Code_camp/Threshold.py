import cv2
import pandas as pd

img = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# cv2.imshow('img', thresh)

adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3) #adaptive threshold requires grayscaled image
cv2.imshow('adaptive', adaptive)

cv2.waitKey(0)