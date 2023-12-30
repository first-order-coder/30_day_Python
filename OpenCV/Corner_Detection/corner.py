import numpy as np
import cv2

image = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')

image = cv2.resize(image, (0, 0), fx=0.75, fy=0.75)
gray_scaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting png into grayscale

'''euclidean distatnce is a measure of how well-separated the detected corners are from each other, A larger minimum distance indicates that 
the algorithm has successfully identified distinct corners that are not too close to each other. This is important for tracking purposes, 
as it prevents redundancy and ensures that the algorithm is focusing on unique and meaningful corner features.'''
                                                        
corners = cv2.goodFeaturesToTrack(gray_scaled_image, 100, 0.01, 10) #
corners = np.intp(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x,y), 5, (255, 0, 0), -1)

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows() 