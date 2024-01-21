def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num -1)

result = factorial(4)
# print(result)

def getEven(n):
    print(n)
    if n == 2:
        return 2
    else:
        return getEven(n-2)
result_2 = getEven(8)
print(result_2)

def getFibbonachi(index_of_number):
    if index_of_number <= 1: #if we give index as 1 or smaller then the value will be exactly them no need to calculate so, our base case is as this.
        return index_of_number
    else:
        return getFibbonachi(index_of_number-1) + getFibbonachi(index_of_number-2) 
result_3 = getFibbonachi(4)
print(result_3)

''' Recursive and Iiterative '''
def walk(steps):
    for step in range(1, steps+1):
        print(step)
walk(10)

def walk_recursive(steps):
    print(steps)  
    walk_recursive(steps-1)
walk_recursive(100) #--> when the function is like this it doesnt have a base condition and will keep going until maximum depth is mathced. we will count 0 and - minus as well.

def walk_recursive(steps):
    if steps == 0:
        return    #to exit the function
    walk_recursive(steps-1)
    print(steps)  
walk_recursive(100)

#factorials_iterative
def factorial(x):
    result = 1
    for y in range(1, x+1):
        result *= y
    print(result)

factorial(5)

#facotrials_recursive
def facotrials_recursive(x):
    if x == 1:
        return 1
    else:
        result = x * facotrials_recursive(x-1)
    return result

print(facotrials_recursive(5))

