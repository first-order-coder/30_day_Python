import numpy as np
import cv2

img = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')

blank = np.zeros(img.shape, dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

canny = cv2.Canny(blur, 125, 175)
cv2.imshow('canny edges', canny)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} founded')
print(hierarchies)

cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow('Contours Drawn', blank)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()