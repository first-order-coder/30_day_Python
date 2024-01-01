import cv2
import numpy as np

img = cv2.imread(r'C:/Users/ginuram/Desktop/Dekstop/30DaysofPython/OpenCV/Assests/base.jpg')
cv2.imshow('img', img)

b, g, r = cv2.split(img)

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

merged = cv2.merge([b, g, r])
cv2.imshow('merged', merged)

blank = np.zeros(img.shape[:2], dtype='uint8') #img.shape[:2] --> if not will raise an error of number of color channels merged, this will take width and height only
# cv2.imshow('blank', blank)                   #the error:--> Invalid number of channels in input image     

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.waitKey(0)
cv2.destroyAllWindows()