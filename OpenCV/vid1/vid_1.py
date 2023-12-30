import cv2
import random

img = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\vid1\vid1.png', 1)
# img = cv2.resize(img, (240, 480))
# img = cv2.resize(img, (0, 0), fx= 0.5, fy= 0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE//3)
# cv2.imwrite('new.png', img)
cv2.imshow('Image', img)
# h, w = img.shape
# print(h)

''' replacing selected pixels in an image'''
# for i in range(50, 100):
#     for j in range(100, 250):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

''' copying a part of an image and pasting it on another place'''
# tag = img[400:600, 100:200]
# img[200:400, 200:300] = tag

# cv2.imshow('Ig', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(img.shape)
