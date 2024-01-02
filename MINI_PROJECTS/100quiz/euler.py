# sum = 0
# for number in range(0, 1001):
#     if number % 3 == 0 and number % 5 == 0:
#         sum = number + sum
# print(sum)

# cap = 4000000

# prev = 0
# curr = 1

# total = 0

# while curr < cap:
#     prev, curr = curr, curr + prev

#     if curr % 2 == 0:
#         total += curr

# print(total)

'''PRIME NUMBER HAS ONLY 2 factors 1 and number itself // 
    composite number has more than 2 factors and also 1 is not a prime number // 
    prime number factoraisation can be shown using exponents as well. 2 * 3^2 '''
''' WHILE loops run untill they are not true'''

'''Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

# def isPrime(x):
#     #If x is even then its not prime, unless x is 2
#     if x == 2:
#         return True
    
#     if x % 2 == 0:
#         return False
    
#     for i in range(3, x, 2): #if number is divisiable by any other than it self its not a prime number
#         if x % i == 0:
#             return (f'{x} is not a prime number')
# print(isPrime(3))

'''PROBLEM 4 
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

'''if the reverse of that number is same as the original number its a palindromic number'''

# a = [] 
# for i in range(1,100):
#     for j in range(1,100):
#         a.append(i * j)

# b = []
# for item in a:
#     item = str(item)
#     if item == item[::-1] and len(item) > 2:
#         b.append(item)
#         c = set(b)

# d = []
# for n in c:
#     d.append(n)
#     d.sort()
# print(max(d))

'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.
What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?'''
'''Least Common Multiple is 1 * 2 * 3 * 4 * 5 * .... * 10
so we can write this as lcm(10) = 2520 sos we can write l(n) = lcm(1,2,...,n)'''



'''Q - 6 Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.'''
''' sum of the squares = 1^2 + 2^2 + 3^2...10^2 
    square of the sum = (1+2+3+4...)^2 = 55^2'''


# sum = 0
# for i in range(1, 101):
#     sum = sum + i ** 2
# # print(sum)

# total = 0
# for j in range(1, 101):
#     total = total + j
#     new_total = total ** 2

# print(f'The Difference between the sum of the squares and square of the sum is:> {new_total - sum}')

'''Q -7 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.


# for i in range(1,11):
#     print(i, end=' ') USING end= function

What is the 10 001st prime number?'''

# def is_prime(n):
#     if n <= 1:
#         return False
    
''' a number is always made up of multiplication of two numbers. when we take the 
    square root of that number we can see one of the factors of that number is always lower than
    the square root and the other can be bigger than square root'''

#     for i in range(2, int(n ** 0.5)+1): # 4**0.5 = sqrt(4) 
#         if n % i == 0:
#            return False
#     return True

# def nth_prime(n):
#     count = 0
#     i =1 
#     while count < n:
#         i += 1
#         if is_prime(i):
#             count += 1
#     return i
# print(nth_prime(10001))

''' Q - 8 Find the thirteen adjacent digits in the 1000-digit number that 
have the greatest product. What is the value of this product?'''

'''Adjacent digits are the digits where there absolute differnece between the position of any number
 is eqauls to 1'''

'''Limits = should be 1000 digits number so 9999 is the maximum'''

# for i in range(1000, 10000):
#     i = str(i)
    
#     if abs(int(i[0]) - int(i[1])) == abs(int(i[1]) - int(i[2])) == abs(int(i[2]) - int(i[3])) == 1:
#         print(i)
    

'''Q - 9 '''

''' Limits = a + b + c = 1000 which means none of them can be more than 1000'''

# for a  in range(1, 1000):
#     for b in range(1, 1000):
#         for c in range(1, 1000):
#             if a + b + c == 1000 and a < b < c and a ** 2 + b ** 2 == c ** 2:
#                 print(a,b,c)
#                 break
'''Also Correct'''
# for b in range(1, 500):
#     if 1000*(500-b) % (1000-b) == 0:
#         print (b, 1000*(500-b) / (1000-b)) 

'''Q - 10 Find the sum of all the primes below two million'''


''' Differnce between two prime number is always 2 or 2s' multiple'''

'''USING factors to get the answer if factors == 0 then its a prime number'''
# x_int = int(23)
# factors = []
# if x_int <= 1:
#     print(f"{x_int} is not a prime number")
    
# else:
#     for factor in range(2, x_int):
#         if x_int % factor == 0:
#             factors.append(factor)
#     if len(factors) == 0: 
#         print(f"{x_int} is a prime number.")
#     else:
#         print(f"{x_int} is not a prime number. It has following factors: {.join(map(str, factors))}.")

''' Finding the prime numbers'''

# def sum_prime(n):
#     is_prime = [True] * n
#     is_prime[0] = is_prime[1] = False

#     for i in range(2, int(n ** 0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, n, i):
#                 is_prime[j] = False
#     return sum(i for i in range(n) if is_prime[i])
# print(sum_prime(5))

''' Q-12 Highly divisible triangular number '''

''' FIND THE DIVISORS OF TRIANGULAR NUMBER '''

# divisiors = []
# for j in triangle:
#     for n in range(1, 29):
#         if j % n == 0:
#           divisiors.append(str(n))
#     divisiors.append('#')
# print(divisiors)

# def num_divisors(n):
#     """Returns the number of divisors of n"""
#     count = 0
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             count += 2
#     return count

''' i and n//i both factors of n beacasue if 28/ i(4) = 7 which means 4 and 7 both factors of n
so the count is incremented by 2'''

# n = 1
# while True:
#     triangle = n*(n+1)//2
#     if num_divisors(triangle) > 500:
#         print(triangle)
#         break
#     n += 1

# num_divisors(500)

''''''
''' Q-14 Longest Collatz sequence '''

# def collatz(n):

#     seq = [n]
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         seq.append(n)
#     return seq 

# max_len = 0
# max_start = 0

# for i in range(1, 1000000):
#     seq_len = len(collatz(i))
#     if seq_len > max_len:
#         max_len = seq_len
#         max_start = i

# print("Startubg", max_start)
        

# def collatz(n):
#     lst = [n]
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         lst.append(n)
#     return lst

# max_len = 0
# max_start = 0

# for i in range(1, 1000000):
#     lst_len = len(collatz(i))
#     if lst_len > max_len:
#         max_len = lst_len
#         max_start = i
# print(max_start)

''' Q - 15 Lattice paths '''
'''Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

number of down moves == number of right moves
2 by 2 grid has total of 4 moves
20 by 20 grid has total of 40 moves

after every 2 rights or 2 downs the end point must be met so, we only have to find 2 downs or 
2 rights out of 4.

The number of ways to choose which 2 steps are the "down" steps out of the 4 
total steps is given by the binomial coefficient "4 choose 2"

How many such routes are there through a 20×20 grid? '''

# import math

# n = 40
# k = 20
# print(math.comb(n,k))

# num_moves = 20
# num_routes = math.comb(num_moves * 2, num_moves)
# print(num_routes)

''' Q - 16 
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000? '''

# n = int(input('Enter the Power:>'))
# amount = str(2 ** n)

# lst = []
# for i in amount:
#     lst.append(i)

# sum = 0
# for n in lst:
#     n = int(n)
#     sum = n + sum
# print(sum)

''' Q-17 Number letter counts Hyphens and string cannot be calculated
using inflect '''

# import inflect

# p = inflect.engine()

# lst = []
# for i in range(1, 1001):
#     a = p.number_to_words(i).replace('- ').replace(' ')
#     length = len(a)
#     lst.append(length)

# sum = 0
# for n in lst:
#     sum += n
# print(sum)

''' Q - 18 Maximum path sum I numbers have to be in a sequance'''

''' numbers that are next to each other in a sequance are called adjacent'''


# triangle = [[75],
#             [95, 64],
#             [17, 47, 82],
#             [18, 35, 87, 10],
#             [20,  4, 82, 47, 65],
#             [19,  1, 23, 75,  3, 34],
#             [88,  2, 77, 73,  7, 63, 67],
#             [99, 65,  4, 28,  6, 16, 70, 92],
#             [41, 41, 26, 56, 83, 40, 80, 70, 33],
#             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#             [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#             [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

# for i in range(len(triangle)-2, -1, -1):
#     for j in range(len(triangle[i])):
#         triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

# print(triangle[0][0])

''' Q-19 How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)? '''

# import calendar

# y = 1901
# m = 1

# a = calendar.month(y,m)
# print(a)

# import datetime

# count = 0
# for year in range(1901, 2001):
#     for month in range(1, 13):
#         # create a datetime object for the first day of the month
#         date = datetime.datetime(year, month, 1)
#         # check if the day is a Sunday
#         if date.weekday() == 0:
#             count += 1
# print(count)

# for year in range(1901, 2001):
#     for month in range(1, 13):
#         print(datetime.datetime(year, month ,1))
        
''' Q-20 Factorial digit sum '''

# import math

# n = int(input('Enter Number:>'))
# a = str(math.factorial(n))

# sum = 0
# for i in a:
#     sum += int(i)
# print(sum)

''' Q - 21 Amicable numbers 
two numbers are amicable if each is equal to the sum of the proper divisors of the other '''

# import time

# start = time.time()

# for a in range(1, 1000):
#     for b in range(1, 1000):
#         # a = 220
#         sum1 = 0
#         for i in range(1, a):
#             if a % i == 0:
#                 sum1 += i
                
#         # b = 284
#         sum2 = 0
#         for j in range(1, b):
#             if b % j == 0:
#                 sum2 += j

#         if sum1 == b and sum2 == a:
#             print(f'Amicable Numbers are: {a} {b}')
# end = time.time()
# print(end - start)

''' Q-22 Names scores USING ORD FUNCTION TO ASSIGN ALPHANUMERIC VALUES TO ALPHABET
    .sort(), insert(), remove() only modifies the original list returns none if printed 
    ord('A') function will give value to Alphabets A - 65, B - 66 so on'''

# with open (r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\p022_names.txtr') as f:
#     names = f.read()
#     a = names.replace('"').split(',')
#     a.sort()  

# sum = 0
# for i in a:
#     place = a.index(i) + 1
#     for letter in i:
#         value = ord(letter) -64
#         sum += value * place
# print(sum)

''' Q - 23 Non-abundant sums '''

''' Perfect Number is a number for which the sum of its propers divisors equals exactly to the 
number '''

''' number (n) is a deficient if the [sum of proper divisors < n] and is called abundant if [sum > n]'''

# for i in range(1, 50):
#     sum = 0
#     for n in range(1, i):
#         if i % n == 0:
#             sum += n

#     if sum > i:
#         print(sum , i)

# lst = [12, 24, 23, 11, 34, 22]
# empty = set()
# for i in lst:
#     for j in lst:
#         sum = i + j
#         empty.add(sum)
# print(empty)

''' Q-24 Lexicographic permutations 
A permuutation is an ordered arrangement of objects. if all of the permutatuins are listed 
numerically or alphabetically we call it lexicographic order'''

''' To calculate permutations we can use permutation function in python itertools library'''

# from itertools import permutations
# import time

# perm = permutations([1, 2, 3])
# perm1 = permutations([1, 2, 3], 2)

# for n in perm1:
#     print(n) #(3, 1),(3, 2)

# for i in perm:
#     print(i) # (3, 1, 2), (3, 2, 1)

# lst = ['GiunuraAmarasena']
# print('@'.join(lst)) #Giunura@Amarasena

''' ANSWER '''
# perm = permutations(['0123456789'])

# count = 0
# start = time.time()
# for i in perm:
#     x = list(i)
#     joined = ''.join(x)

#     count += 1
#     if count == 1000000:
#         print(joined)
#         break
# end = time.time()
# print(f' IT TOOK {end - start}')
    # print(joined, '--------------',count)

''' Q-26 Reciprocal cycles 
A unit fraction contains 1 in the numerator. '''

'''Q-28 Number spiral diagonals'''

''' only ODD numbers are in diagonal / for every square formed only 4 diagonal elemants are there
    but they all are odds as well '''

''' 1st sqaure - Gap = 0
    2nd square - Gap = 1
    3rd square - Gap = 2
    4th square - Gap = 3
    
    they all are odd numbers as well'''

# import time

# start = time.time()
# last_number = 1001 * 1001 # size is 1001 by 1001 so max number is 1001 * 1001
# odd_numbers = range(1, last_number + 1, 2)

# lst = []
# for i in odd_numbers:
#     lst.append(i)
# print(lst)

# import random
# import string

# for _ in range(10):
#     result = ''.join(random.choices(string.ascii_letters + string.ascii_uppercase + string.digits, k=5))
#     print(result)

''' Q-29 Distinct Powers'''

# lst = []
# for a in range(2, 101):
#     for b in range(2, 101):
#         square = a ** b
#         lst.append(square)
# nwlst = sorted(set(lst))
# print(len(nwlst))

''' Q-30 Digit fifth powers '''

# for num in range(1000, 100000):
#     num = str(num)
#     num1 = int(num[0]) ** 5 + int(num[1]) ** 5 + int(num[2]) ** 5 + int(num[3]) ** 5

#     if int(num) == num1:
#             print(num)


from itertools import count

''' Q-32 Pandigital products an n-digit number is pandigital if it 
    makes use of all the digits 1 to n exactly once
    
    multiplicand = 12, multiplier = 2, product= 24 '''

# index = count()
# lst = []

# for i in range(40):
#     for n in range(187):
#         multi = i * n

# multi = str(multi)
# i = str(i)
# n = str(n)

''' If the lists have different lengths, the zip() 
function will stop iterating once it reaches the end of the shortest list.'''

'''trying to access them outside the loops. This will only store the 
last values assigned to these variables, rather than the values obtained from the loops.'''

# for item1 in (multi):
#     lst.append(item1)
# for item2 in (i):
#     lst.append(item2)
# for item3 in (n):
#     lst.append(item3)

# lst = sorted(set(lst))    

''' Q-33 Digit cancelling fractions '''

''' Q-34 Digit factorials 
-Find the sum of all numbers which are equal to the sum of the factorial of their digits.''' 

''' for this we can straight up use the math.factorial method in python because it has C type
internal implementation because of that it is fast.'''

# import math

# total = 0
# for i in range(3, 1001):
#     sum = 0
#     for digit in str(i):
#         sum += math.factorial(int(digit))
#     if sum == i:
#         total += i
# print(total)

''' Q-35 Circular primes 
circular are called circular primes because when their digits are rotated the new number it
outputs is also a prime number '''

import random

# def primes(x):
#     for number in range(2, x):
#         if x % number == 0:
#             return (f'{x} is not a prime number')
#         else:
#             return ('is a prime number')
# print(primes(197))

''' Understand the working mechanism of the loops '''

# lst = []
# for i in range(2, 16):
#     for n in range(2, i):
#         if i % n == 0:
#            break
#     else:
#         lst.append(i)
# # print(lst)

# list1 = []
# for item in lst:
#     length = len(str(item))
#     item = str(item)
#     for index in range(0, length):
#         list1.append(item[index:] + item[:index])
# print(list1)


# print(random.shuffle(str(23))) #shuffle use list of items and shuffle them in random order

# lst = ['1972']
# print(lst[1:]) #digits starting from index 1
# print(lst[:1]) #digits from the beginning up to index 1

# print(lst[1:] + lst[:1])  rotated version of original lst 

''' Q-36 Double-base palindromes '''
''' decimal system are base 10 from 1 to 10, binary systems are 0 and 1'''

'''decomal to binary using built in function ----> you can simply use the bin() function to convert 
    from a decimal value to its corresponding binary value.'''

'''int() function to convert a binary to its decimal value'''

# a = 79

# #to bin
# bin_A = bin(a)
# print(bin_A)
# print(int(bin_A, 2))

# lst = ['1234']
# print(lst[::-1])

''' Answer '''
# palnidromic_nums = []
# for i in range(1, 1000):
#     # new_lst = []
#     number = str(i)
#     if number[::-1] == number:
#         palnidromic_nums.append(number)

# lst = []
# for item in palnidromic_nums:
#     binary = str(bin(int(item)))
#     only_binary = binary[2:]
#     if only_binary[::-1] == only_binary:
#         lst.append(item)
# print(lst)

# print(palnidromic_nums)

''' This part was unnecassary '''
#     for n in number:
#         new_lst.append(n)
#         palindo = ''.join(new_lst[::-1])
#         if int(palindo) == i:
#             palnidromic_nums.append(i)
# #print(palnidromic_nums)
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''

''' This is unneccasry too'''
#     for digit in binary[2:]:
#         lst.append(digit)
#         palindromic = int(''.join(lst[::-1]))
#         if palindromic == int(binary[2:]):
#             new_pal.append(item)
# print(new_pal)
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''

# def is_palindrome(n):
#     # Check if a number n is a palindrome in base 10
#     return str(n) == str(n)[::-1]

# def is_binary_palindrome(n):
#     # Check if a number n is a palindrome in base 2
#     binary = bin(n)[2:]  # Convert to binary and remove "0b" prefix
#     return binary == binary[::-1]

# def find_palindromic_numbers():
#     palindromic_numbers = []
#     for i in range(1, 1000):
#         if is_palindrome(i) and is_binary_palindrome(i):
#             palindromic_numbers.append(i)
#     return palindromic_numbers

# # Find all palindromic numbers
# result = find_palindromic_numbers()
# print(result)

# ls = [i for i in range(0,5)]
# print(ls)

# t1 = (1, 2)
# t2 = (3, 4)
# print(t1-t2)

'''Q-37 '''

# sting = input('Enter:>')
# print(sting.split(' '))

# def my_func(num):
#     if num == 5:
#         return ['Python']
#     else:
#         yield from range(num)
# print(my_func(5))
# import pandas as pd

# df = pd.read_csv(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\MINI_PROJECTS\100quiz\Market_Basket_Optimisation.csv', header= None)

# x = []
# x1 = []
# for j in range(0, 7501):
#   for i in df.iloc[j, :]:
#     x.append(i)
#   x1.append(x)
# print(x1)

# from collections import Counter
# print(Counter(char_input))

# char_input = input("Enter Characters:>").replace(' ', '')
# new_lst = []
# for i in char_input:
#     new_lst.append(i)

# special_signs = ['!#@$%^&*+.=-,?/><']

# alphabetics = {}
# for char_1 in char_input:
#     if char_1.isalpha():
#         alphabetics[char_1] = char_input.count(char_1) #Dictionary keys are unique, so each character will only be counted once.
# for count2,alpha in alphabetics.items():
#     print(count2, alpha)


# count1 = 0
# for char in char_input:        
#     for sign in special_signs:
#         if char in sign:
#             count1 = count1 + 1
# print('Non_Alphabetical_Count:', count1)

# import pyautogui

# def blur_screen():
#     # Perform the action to blur the screen here (e.g., using OS-specific commands)
#     # Replace the following line with the appropriate code for your OS (e.g., Windows, macOS, Linux).
#     # This example will move the mouse to a corner of the screen (0, 0).
#     pyautogui.moveTo(0, 0)

# if __name__ == "__main__":
#     pyautogui.FAILSAFE = False  # Disable fail-safe to allow sudden swipes without interruption
#     try:
#         while True:
#             x1, y1 = pyautogui.position()
#             pyautogui.sleep(0.1)  # Wait for a short time (adjust as needed)
#             x2, y2 = pyautogui.position()
#             if (x1, y1) != (x2, y2):  # Check if there was a mouse movement (swipe)
#                 blur_screen()  # Call the function to blur the screen
#     except KeyboardInterrupt:
#         pass

# '''Q-38 Pandigital Multiples'''

# empty = set()
# lst = []

# for i in range(9, 10):
#     for j in range(1, 6):
#         answer = str(i * j)
#         lst.append(answer.split())
#         lst.sort()
#         # empty.add(answer) 
# print(lst)

# import time
# from datetime import datetime
# start = datetime.now()
# name = 'Ginura Maneth Amarasena'
# for i in name:
#     print(i, end='')
#     time.sleep(0.1)
# end = datetime.now()

# print('\n', end-start)

# anode = int(input('Anode Value:>>'))
# cathode = int(input('Cathode Value:>>'))

# if anode > cathode + 0.7:
#     print('Curent Will Flow')
# else:
#     print('Current Will not flow')

from datetime import datetime

t_1 = datetime.now()
password = int(input('Enter A Number::>'))

for i in range(0, 100000):
    if i == password:
        print(i, password)
        print('Matched')
        
t_2 = datetime.now()
print(f'It took {t_2-t_1}')

# print(datetime.now())