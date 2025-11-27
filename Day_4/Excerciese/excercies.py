from itertools import chain
from unicodedata import name


Challenge = 'Coding For All'
print(Challenge.split(' ')) #will split the string from given sepeartor(between the semi columns), and put them all in a list
print(Challenge[2])

names = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(names.split(','))

print(Challenge[0])

index = len(Challenge) -1
result = Challenge[index]
print(result)
print(index)
