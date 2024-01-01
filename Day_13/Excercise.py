# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# neg_zero = [i for i in numbers if i <= 0]
# print(neg_zero)

# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# falttened = [num for row in list_of_lists for num in row]
# print(falttened)


# tple = [ (i, 1, i * 1, i **2, i ** 3, i **4, i **5) for i in range(11) ]
# for x in tple:
#     print(x)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# flattened = [ coun for row in countries for coun in row ]
# print(flattened)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# dict = {'Ginura'}
# print(dict)

tple = [(i, i *2, i *3, i *4, i *5) for i in ['#','@','%','^','*']]
for x in tple:
    print(x)
