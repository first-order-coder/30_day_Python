import random
rn = [random.randint(0, 100) for _ in range(100)]
# print(rn)

#removing duplicate items from a list
list = [1, 1, 2, 2, 3, 4, 3, 5, 3, 4]
set = set(list)
# print(set)

#joining two dicts
dict = {'a': 2, 'b': 3, 'c': 4}
dict1 = {'ac': 1, 'bc': 23, 'va': 22}

new_dict = dict.update(dict1)
# print(dict)

def summation(*numbers):
    return sum(numbers)
# print(summation(1, 2, 3, 4, 5))

