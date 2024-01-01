import numpy as np
import cv2

img = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\8067240_orig.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgGray, (7,7), 1)

img_canny = cv2.Canny(imgblur, 50, 50)#if a pixel gradient is higher than the upper threshold then it is considered as a edge otherwise no.

# blank = np.zeros((900, 900), dtype='uint8')

# cv2.imshow('blank', img_canny)

imgContour = img.copy()

def getContours(img):
    contours, hierarchies = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    for contour in contours:

        area = cv2.contourArea(contour)
        # print(area)

        cv2.drawContours(imgContour, contour, -1, (255, 0 , 0), 3)
        cv2.imshow('Drawed', imgContour)

        perimeter = cv2.arcLength(contour, True)
        # print(perimeter)
        
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        print(len(approx))

        object_corners = len(approx)
        x, y, w, h = cv2.boundingRect(approx)

        if object_corners == 3:
            objectType = "Triagonal"
            
        elif object_corners == 4:

            aspratio = w/float(h)
            if aspratio > 0.95 and aspratio < 1.05:
                objectType = "Square"
            else:
                objectType = "Rectangle"

        elif object_corners > 4:
            objectType = "Circle"
        
        else:
            objectType = "None"
        
        cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))

getContours(img_canny)
cv2.waitKey(0)
