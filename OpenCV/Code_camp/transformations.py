import numpy as np
import cv2

image = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')

# def translate(img, x, y):
#     transmatrix = np.float32([[1,0,x], [0,1,y]])
#     dimensions = (image.shape[1], image.shape[0])
#     return cv2.warpAffine(img, transmatrix, dimensions)

# translated = translate(image, 100, 100)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()