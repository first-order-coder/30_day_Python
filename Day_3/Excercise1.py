import math
import cmath


Y_1 = float(input('Enter Y1:'))
Y_2 = float(input('Enter Y2:'))
X_1 = float(input('Enter X1:'))
X_2 = float(input('Enter X2:'))

Slope_M = (Y_2 - Y_1) / (X_2 - X_1) 

print(int(Slope_M))

Ecuidean_Distance = (Y_2 - Y_1) ** 2 + (X_2 - X_1) ** 2

print(Ecuidean_Distance)

print(math.sqrt(Ecuidean_Distance))

print(math.sqrt(81))