import cv2

image = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')
gray_scaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting png into grayscale

edges = cv2.Canny(gray_scaled_image, 110, 200)
edges2 = cv2.Canny(gray_scaled_image, 150, 250)
edges3 = cv2.Canny(gray_scaled_image, 200, 300)

cv2.imshow('Image', edges)
cv2.imshow('Image2', edges2)
cv2.imshow('Image3', edges3)

cv2.waitKey(0)
cv2.destroyAllWindows() 