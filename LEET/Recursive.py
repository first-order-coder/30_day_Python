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
# result_2 = getEven(8)
# print(result_2)

def getFibbonachi(index_of_number):
    if index_of_number <= 1: #if we give index as 1 or smaller then the value will be exactly them no need to calculate so, our base case is as this.
        return index_of_number
    else:
        return getFibbonachi(index_of_number-1) + getFibbonachi(index_of_number-2) 
result_3 = getFibbonachi(4)
print(result_3)