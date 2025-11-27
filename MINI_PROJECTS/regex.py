from collections import Counter, defaultdict
from email.policy import default
from statistics import*
from itertools import count
import re
from turtle import distance
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'

# temp = [wrd for sub in paragraph for wrd in sub.split()] #nested list comprehensions
temp = defaultdict(int)

txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
regex = r'-?\d+'
matches = re.findall(regex, txt)

for i in range(0, len(matches)):
    matches[i] = int(matches[i])
print(matches)


distance1 = max(matches)
distance2 = min(matches)
distance = distance1 - distance2
print(distance)