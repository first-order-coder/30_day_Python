# import imp
# import re


# def add_numbers(num1, num2):
#     sum = num1 + num2
#     return sum
# print(add_numbers(5,8))

# from cmath import pi

# def area_of_a_circle(r):
#     area = pi * (r**r)
#     return(area)
# print(area_of_a_circle(10))

# def add_all_numbers(*n):
#     total = 0
#     for i in n:
#         total = total + i
#     return total
# print(add_all_numbers(2,3,5))

# def convert_celcius_to_fahrenheit(temp):
#     f = temp * (9 / 5) +32
#     return f
# print(convert_celcius_to_fahrenheit(100))

# def check_season(month):
#     Winter = ['December', 'January', 'February']
#     Autmn = ['September', 'October', 'November']
#     Spring = ['March', 'April', 'May']  
#     Summer = ['June', 'July', 'August']

#     if month in Winter:
#         return 'Its Winter Season'

#     elif month in Autmn:
#         return 'Its Autmn Season'

#     elif month in Spring:
#         return 'Its Spring Season'

#     elif month in Summer:
#         return 'Its Summer Season'

# print(check_season('January'))

# from cmath import sqrt


# def calculate_slope(x, y):
#     slope = sqrt( x**2 + y**2)
#     return(slope)
# print(calculate_slope(5, 12))

# def print_list():
#     list = ['Ginura', 'Amarasena', 'Maneth']
#     for i in list:
#         print(i)
# print(print_list())

# def reverse_list():
#     list = [1, 2, 3, 4, 5]
#     for i in reversed(list):
#         print(i, end= " ")
#     return(reverse_list)
# reverse_list ()

# def reverse_list1():
#     list1 = ['A', 'B', 'C']
#     for num in reversed(list1):
#         print(num, end= " ")
#     return(reverse_list1)
# reverse_list1()

# def add_item(item):
#     food_staff = ['Potato','Tomato', 'Mango', 'Milk']
#     food_staff.append(item)
#     return(food_staff)
# print(add_item('Orange'))    

# def remove_item(item1):
#     food_staff = ['Potato','Tomato', 'Mango', 'Milk']
#     food_staff.remove(item1)
#     return(food_staff)
# print(remove_item('Mango'))

# def sum_of_numbers(number):
#     sum = 0
#     for i in range(0, number+1):
#         sum =sum + i
#     return(sum)
# print(sum_of_numbers(5))

# def even_and_odds(num):
#     numbers = range(num + 1)
#     even_count, odd_count =0, 0
#     for numb in numbers:
#         if numb % 2 == 0:
#             even_count += 1
#         elif numb % 2 != 0:
#             odd_count += 1
#     return('Even Count:', even_count,'Odd Count:', odd_count)
   
# print(even_and_odds(100))
             
from turtle import end_fill


def reverse_list():
    list = [1, 2, 3, 4, 5]
    for i in reversed(list):
        print(i, end=' ')
reverse_list()