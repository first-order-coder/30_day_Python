from collections import Counter, defaultdict
from email.policy import default
from statistics import*
from itertools import count
import re
from turtle import distance

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'

txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
# regex = r'-?\d+'
# matches = re.findall(regex, txt)

# for i in range(0, len(matches)):
#     matches[i] = int(matches[i])
# print(matches)
# txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

# #re.I means both uppercases and lowercases are included.

# match = re.findall('python', paragraph, re.I)
# print(match)

# #without re.I
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'

# match1 = re.findall('[Pp]ython', paragraph)
# print(match1)

# #replaceing a substring. Have to give the exact string that needs to be replaced
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'
# match_replace = re.sub('Python', 'Java', paragraph, re.I)
# print(match_replace)

# # distance1 = max(matches)
# # distance2 = min(matches)
# # distance = distance1 - distance2
# # print(distance)

# lst = ['FI', 'GE', 'UK', 'AS']
# match2 = re.findall('FI', lst, re.I)
# print(match2)

print(re.split('love ', paragraph))
# string = 'My name is ginura'
# print(string.replace('name', 'age'))
# def sum_of(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of(*lst))