import numpy as np  
import cv2
import time

path = r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg'

def empty(a):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)

cv2.createTrackbar('HUE MIN', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('HUE MAX', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('SAT MIN', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('SAT MAX', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('VAL MIN', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('VAL MAX', 'TrackBars', 255, 255, empty)

while True:
    img = cv2.imread(path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('HUE MIN', 'TrackBars')
    h_max = cv2.getTrackbarPos('HUE MAX', 'TrackBars')
    s_min = cv2.getTrackbarPos('SAT MIN', 'TrackBars')
    s_max = cv2.getTrackbarPos('SAT MAX', 'TrackBars')
    v_min = cv2.getTrackbarPos('VAL MIN', 'TrackBars')
    v_max = cv2.getTrackbarPos('VAL MAX', 'TrackBars')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_img, lower, upper)
    masked = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow('HSV', hsv_img)
    cv2.imshow('masked', masked)
    # cv2.imshow('MASKED', mask)
    # cv2.imshow('Orginal', img)

    cv2.waitKey(1)
