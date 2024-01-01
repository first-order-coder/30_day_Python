import numpy as np
import cv2

blank = np.zeros((500, 500), dtype='uint8')
# cv2.imshow('blank', blank)

''' in this case beacuse we used the original blank copy we drawed every shape in same blank page. We need to make copy of blank, 
that way we will get two seperate images of circle and rectangle'''

circle = cv2.circle(blank.copy(), (250, 250), 180, (255,255,255), -1) 
rectangle = cv2.rectangle(blank.copy(), (100, 100), (400, 400), (255, 255, 255), -1)
# cv2.imshow('circle', circle)
# cv2.imshow('rectangle', rectangle)

#bitwise_and(&) --> only intersecting points (if both bits match each other then its 1 if not 0)
bitwise_and = cv2.bitwise_and(circle, rectangle)
cv2.imshow('bitwise_and', bitwise_and)

#bitwise_OR(|) --> non intersecting + intersecting points all are considered (if one of the bits is 1 then output is 1)
bitwsied_or = cv2.bitwise_or(circle, rectangle)
cv2.imshow('bitwise_or', bitwsied_or)

#bitwise_XOR --> non intersecting regions
bitwsied_XOR = cv2.bitwise_xor(circle, rectangle)
cv2.imshow('bitwised_XOR', bitwsied_XOR)

#bitwise_NOT --> the opposite ( flipping bits 0->1 and 1->0 )
bitwise_NOT_rectangle = cv2.bitwise_not(rectangle)
bitwise_NOT_circle = cv2.bitwise_not(circle)
cv2.imshow('bitwise_not', bitwise_NOT_circle)

cv2.waitKey(0)
cv2.destroyAllWindows()