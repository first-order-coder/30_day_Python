import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


img = cv2.imread(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\OpenCV\Assests\base.jpg')

color = ('b', 'g', 'r')
for index, colo in enumerate(color):
    hist = cv2.calcHist([img], [index], None, [256], [0, 256])
    plt.plot(hist, color= str(colo)) #the color has to a string otherwise it wont work
    plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
