# lst = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
# print(lst)


# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))

# print (','.join(l))
import random
# #Q2

# rn = [random.randint(0, 100) for _ in range(100)]
# print(rn)

#Q3

# n = int(input('n: '))

# dict = {}
# for i in range(1, n+1):
#     dict[i] = i*i
# print(dict)

#Q4

# numbers = input('Enter Numbers:')
# new = numbers.split(',')
# tuple = tuple(new)
# print(new)
# print(tuple)

#Q5
'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

# class test1(object):
    
#     def __init__(self, string):
#         self.string = string
    
#     def getString(self):
#         return self.string
    
#     def printString(self):
#         print(self.string)
    
# str1 = test1('Ginura')
# print(str1.getString())
# str1.printString()

'''Q6 - Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.'''

# C = int(50)
# H = int(30)
# Numbers = input('Enter Numbers:')
# Numberslst = Numbers.split(',')

# import math

# value = []
# for D in Numberslst:
#     value.append(str(int(round(math.sqrt((2 * C * float(D)) / H )))))
# print(','.join(value))

'''Q8 - Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated 
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world '''

# input = input('Enter: ').split(',')
# input.sort()
# print(input)
# print(','.join(input))

'''Q9 - Write a program that accepts sequence of lines as input and prints the lines after making all characters in 
the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world Practice makes perfect
Then, the output should be:
HELLO WORLD PRACTICE MAKES PERFECT '''

# string = input('Enter: ').upper()
# print(string)

'''Q-10 
Write a program that accepts a sequence of whitespace separated words as input and prints the words after 
removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''

# string = input('Enter: ').split(' ')
# string.sort()
# print(' '.join(string))

'''Q-11 Write a program which accepts a sequence of comma separated 4 digit binary numbers as its 
input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to 
be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.'''

# numb = input('Enter Numbers: ').split(',')
# lst = []
# for i in numb:
#     i = int(i)
#     if i % 5 == 0:
#         lst.append(i)
# n1, n2 = lst
# print(f'0{n1},{n2}')
import re
'''Q-12 Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''
#split means where do u wanna break it from !!!
# sentence = input('Enter Sentence: ')

# regex = r'[A-Z,a-z]'
# matches2 = re.findall(regex, sentence)

# regex_pattern = r'\d'
# matches = re.findall(regex_pattern, sentence)

# print(f'LETTERS = {len(matches2)}\nDIGITS = {len(matches)}')

'''Q-13 Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each 
digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

# answer = []
# empty = []

# for number in range(1000, 3001):
#     s = str(number)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
#         empty.append(s)
# print(','.join(empty))

'''Q-14 Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

# sentence = input('Enter Sentence: ')
# regex_pattern1 = r'[A-Z]'
# regex_pattern2 = r'[a-z]'
# match1 = re.findall(regex_pattern1, sentence)
# match2 = re.findall(regex_pattern2, sentence)

# print(f'UPPER CASE = {len(match1)}\nLOWER CASE = {len(match2)}')

'''Q-15 Write a program that computes the value of a+aa+aaa+aaaa with a 
given digit as the value of a.
Suppose the following input is supplied to the program: 9
Then, the output should be: 11106'''

# numb = int(input('Give Digit: '))
# sequance = f'{numb} + {numb}{numb} + {numb}{numb}{numb} + {numb}{numb}{numb}{numb}'.split('+')

# numbers = []
# for item in sequance:
#     item = int(item)
#     numbers.append(item)

# sum = 0
# for n in numbers:
#     sum = n + sum
# print(sum)

'''Q -16 Use a list comprehension to square each odd number in a list. The list is input by a sequence 
of comma-separated numbers.
Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9
Then, the output should be: 1,3,5,7,9'''

# numbers = input('Enter Numbers: ').split(',')
# lst = [i for i in numbers if int(i) % 2 != 0]
# print(','.join(lst))

'''Q -17 Write a program that computes the net amount of a bank account based a 
transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500'''

# sum = 0
# tarnsactions = input('Enter Amount Followed By D or W and Comma(,): ').replace(',', '').split('|')
# for item in tarnsactions:
#     item = float(item)
#     sum = item + sum
# print(sum)
# # 929,957.41|341,447.97


# tarnsactions = input('Enter Amount Followed By D or W and Comma(,): ').split(',')

# sum = 0
# for item in tarnsactions:
#     if 'D' in item:
#         d = int(item.strip(item[0]))
#         sum = d + sum
    
#     elif 'W' in item:
#         w = int(item.strip(item[0]))
#         sum = sum - w
# print(sum)

'''Q-18 A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check 
them according to the above criteria. Passwords that match the criteria are to be printed, 
each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
# import re

# passwords = input('Enter Passwords follwed By ,: ').split(',')

# for password in passwords:
    
#     match_1 = re.findall(r'[a-z]', password)
#     match_2 = re.findall(r'[A-Z]', password)
#     match_3 = re.findall(r'[0-9]', password)
#     match_4 = re.findall(r'[$#@]', password)

#     if match_1 == []:
#         # print('Simple Missing')
#         continue
#     elif match_2 == []:
#         # print('Capital Missing')
#         continue
#     elif match_3 == []:
#         # print('Digit Missing')
#         continue
#     elif match_4 == []:
#         # print('Special Character Missing')
#         continue
#     elif len(password) > 12 or len(password) < 6:
#         # print('Length is Wrong')
#         continue
#     else:
#         print(password)


'''Question:19
You are required to write a program to sort the (name, age, height) tuples by 
ascending order where name is string, age and height are numbers. The tuples are input by 
console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

# l = []
# while True:
#     s = raw_input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))

'''Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n.'''

'''Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of 
movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:2'''
from math import sqrt

# up = int(input("UP:"))
# down = int(input("DOWN:"))
# left = int(input("LEFT:"))
# right = int(input("RIGHT:"))

# y_distance = abs(up - down)
# x_distance = abs(left - right)

# distance = sqrt(y_distance ** 2 + x_distance ** 2)
# print(int(float(distance)))

# pos = [0,0]

# while True:
#     s = input("ENTER:>")
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])

#     if direction == "UP":
#         pos[1] += steps
#     elif direction == "DOWN":
#         pos[1] -= steps
    
#     elif direction == "LEFT":
#         pos[0] -= steps
#     elif direction == "RIGHT":
#         pos[0] += steps
    
#     else:
#         pass

# print(int(float(sqrt(pos[1] **2 + pos[0] ** 2))))

'''Q-22 Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1 '''

# sorted(list_name, reverse= True)

# sentence = input("Enter Desired Sentence:>").split(" ")
# set1 = set(sentence)

# for i,j in zip(sorted(set1), sorted(sentence)):
#     print(f'{i}:{sentence.count(i)}')


'''Q-23 Write a method which can calculate square value of a number'''

# def square():
#     number = int(input("Enter Number:>"))
#     return number ** 2
# print(square())

# print(number ** 2) :: BOTH WORK FINE
# square()

# x = lambda x, y, z : x ** 2 + y ** 2 + z ** 2
# print(x(2,3,4))

# def square(n):
#     return lambda x: n ** x
# x = square(5)
# print(x(2))

lst = [1, 2, 3, 4, 5, 6, 8, 9]
# print(list(filter(lambda x: x % 2 == 0, lst)))
# print(list(map(lambda x: x **2, lst )))

'''Question 25:
    Define a class, which have a class parameter and have a same instance parameter.'''

# class Dog(object):

#     name = 'person'
    
#     def __init__(self, name):
#         self.name = name
#         pass

'''Question:
Define a function which can compute the sum of two numbers.'''

# def sum(x, y):
#     return x + y

# print(sum(10,20))

'''Q -27 Question:
Define a function that can convert a integer into a string and print it in console.
'''

# def convert_int_to_string(n):
#     return str(n)
# print(convert_int_to_string(type(10)))

'''Q - 28 Define a function that can receive two integral numbers in string 
form and compute their sum and then print it in console.'''

# def printValue(s1,s2):
# 	print int(s1) + int(s2)

# printValue("3","4") 

'''Q - 29 Define a function that can accept two strings as input and 
concatenate them and then print it in console.'''

# def join(str1, str2):
#     return str1 + str2
# print(join('Ginura ', 'Amarasena'))

'''Q - 30 Define a function that can accept two strings as input and print the 
string with maximum length in console. If two strings have the same 
length, then the function should print all strings line by line.'''

# def length(str1, str2):
#     if len(str2) > len(str1):
#         print(str2)
#     elif len(str2) <  len(str1):
#         print(str1)
#     else:
#         print(f'{str1}\n{str2}')

# length('Ginura', 'Maneth')

'''Q - 31 Define a function that can accept an integer number as input and
    print the "It is an even number" if the number is even, otherwise 
    print "It is an odd number".'''

# def odd_or_even(n1):
#     if n1 % 2 == 0:
#         print('It is an even number')
#     else:
#         print('It is and odd number')
# odd_or_even(11)

'''Q - 32 Define a function which can print a dictionary where the keys 
are numbers between 1 and 3 (both included) and the values are square of keys.'''

# def sqaure_dict(n):
#     a = {}
#     for i in range(0, n):
#         a[i] = i ** 2
#     print(a)
# sqaure_dict(4)

'''Q-33 Define a function which can generate a dictionary where the keys are 
numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the values only.
'''

# def sqaure_dict(n):
#     a = {}
#     for i in range(0, n):
#         a[i] = i ** 2
#     print(a.values()) #using paranthesis will solve the problem of ''<built-in method values of dict object at''
# sqaure_dict(4)

'''Q -34 Define a function which can generate and print a 
list where the values are square of numbers between 1 and 20 (both included).'''

# def square(n):
#     a = [(i, i ** 2) for i in range(1, n)]
#     return a
# print(square(10))

'''Q - 35 '''

# dict = {'KEY!': 'GINURA', 'KEY2':'AMARASENA', 'KEY3':'MANRTGH'}
# print(dict)

''' Q-36 Define a function which can generate a list where the values are 
square of numbers between 1 and 20 (both included). Then the function needs to 
print the last 5 elements in the list. '''

add = lambda x,y : x + y
print(add(10, 20))
