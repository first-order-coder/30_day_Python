from cmath import pi
from itertools import product
from math import remainder

first_name = 'ginura'
last_name = 'Amarasena'
full_name = 'Ginura Amarasena'
country = 'Sri Lanka'
City = 'Colombo'
age = 21
year = 2022
is_married = False #boolean values
is_true = 1
is_ligt_on = 1
first_name, last_name, country = 'Ginura', 'Amarasena', 'Sri'

print(type(first_name)) #gives the type of the first_name 
print(type(last_name)) #type of the name whether a string or what
print(type(full_name))
print(type(country))
print(type(is_married))
print(len(first_name)) #gives the length of the passed string
print(len( last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two #taking the exponential 
floor_division = num_one // num_two #will divide and round the number to the nearest whole number

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

radius = 30
area_of_circle1 = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius


print(area_of_circle1)
print(circum_of_circle)

radius_input = float(input('Radius:  '))
area_of_circle = pi * radius_input * radius_input
print(type(radius_input))
print(area_of_circle)
