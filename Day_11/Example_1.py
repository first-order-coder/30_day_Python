# # import re


# # def sum_of_numbers(n):
# #     total = 0
# #     for i in range(n+1):
# #         total += i
# #     return total
# # print(sum_of_numbers(100))

# # # from cmath import pi


# # # def area_of_a_circle (r):
# # #     area = pi * r **2
# # #     return area
# # # print(area_of_a_circle(10))

# # def greetings(name ='peter'):
# #     message = name +', Welcome To Python'
# #     return message
# # print(greetings)
# # print(greetings('Asabaneh'))

# # #You can pass functions around as parameters
# # def square_number (n):
# #     return n * n
# # def do_something(f, x):
# #     return f(x)
# # print(do_something(square_number, 3)) # 27

# def main():
#     x = int(input('Enter X:'))
#     if is_even (x):
#         print('x is even')
#     else:
#         print('x is odd')

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# main()

import re


def fizzBuzz(n):
    for i in range(1, n+1):
        
        if i / 3 == 0 and i / 5 == 0:
             print('FizzBuzz')
        
        elif i / 3 == 0:
            print('Fizz')
        
        elif i / 5 == 0:
            print('Buzz')
        
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            
        else:
            print(i)
             
print(fizzBuzz(15))
