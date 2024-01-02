import re
def sum_num(nums):
    return sum(nums)

def high_or_fun(f, lst):
    summation = f(lst)
    return summation
result = high_or_fun(sum_num, [1, 2, 3, 4, 5])

print(result) 

def square(x):
    return x **2
def cube(x):
    return x **3
def abos(x):
    if x >= 10:
        return x
    else:
        return -(x)

def hig_order(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'abos':
        return abos

result = hig_order('square')
print(result(3))

result = hig_order('cube')
print(result(3))

result = hig_order('abos')
print(result(-3))
