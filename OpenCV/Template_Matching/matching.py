import numpy as np
import cv2

image = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg', 0)
temp = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\temp2.jpg', 0)
height, width = temp.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = image.copy()
    
    result = cv2.matchTemplate(img2, temp, method) #this is going to perform convolutional on image, it will take template image and move it across base image
                                                   #to see which parts matches the most

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right_corner = (location[0] + width, location[1] + height)
    cv2.rectangle(img2, location, bottom_right_corner, 150, 3)
    cv2.imshow('Image', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()