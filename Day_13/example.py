# from audioop import add
# from tkinter import N
import random
import string


# numbers = [i for i in range(11)]
# print(numbers)

# numb = [i * i for i in range(11)]
# print(numb)

# num = [(i, i * i) for i in range(11)]
# print(num)

# even_numbers = [i for i in range(21) if i % 2 == 0]
# print(even_numbers)

# odd_numbers = [i for i in range(21) if i % 2 != 0]
# print(odd_numbers)

# numbers1 = [-9, -8, -3, 0, 1, 2, 4, 22, 12, 5]
# positive_even = [i for i in numbers1 if i % 2 == 0 and i > 0]
# print(positive_even)

# def add_two_numbers(a, b):
#     return a + b
# print(add_two_numbers(2,3))

# add_two = lambda a,b: a + b
# print(add_two(2,3))

# add = lambda a,b,c : a * b -c
# print(add(2, 3, 4))

# # square = lambda x: x ** 2
# # print(square(3))

# # mulitple = lambda a, b, c: a ** 2 -3 * b + 4 * c
# # print(mulitple(5, 5, 3))

# # def power(x):
# #     return lambda n: x ** n

# # print(power(2)(3))

# language = 'Python'
# print(list(language[0:6]))

# lst = [i for i in language]
# print(lst)

num_id = int(input('number of IDS:'))
char_len = int(input('Char length:'))
char_len1 = int(char_len / 2)
char_len2 = int(char_len / 2)


for _ in range(0,num_id + 1):
    method1 = ''.join(random.choices(string.ascii_letters + string.hexdigits, k= char_len1))
    method2 = ''.join(random.choices(string.ascii_letters + string.hexdigits, k= char_len2))
    method = method1 +' '+ method2
    print(method)
    # print(method2)

