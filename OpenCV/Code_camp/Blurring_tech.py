import cv2

img = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')
cv2.imshow('base_image', img)

#average blur
average_blur = cv2.blur(img, (7,7))
# cv2.imshow('average', average_blur)

#Gaussian
gaussian_blur = cv2.GaussianBlur(img, (7,7), 1)
# gaussian_blur2 = cv2.GaussianBlur(img, (7,7), 4)
# gaussian_blur3 = cv2.GaussianBlur(img, (7,7), 7)
cv2.imshow('gaussian', gaussian_blur)
# cv2.imshow('gaussian2', gaussian_blur2)
# cv2.imshow('gaussian3', gaussian_blur3)

#median_blur 
median = cv2.medianBlur(img, 3)
cv2.imshow('median', median)

#bilateral blur --> better because it apply the blurring but retain the edges
bilateral = cv2.bilateralFilter(img, 5, 15, 15)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
