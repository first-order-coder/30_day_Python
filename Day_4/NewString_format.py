first_name = 'Ginura'
last_name = 'Amarasena'

language = 'python'

formatted_strings = 'I am {} {} and I learn {}'.format(first_name, last_name, language)
print(formatted_strings)

a = 4
b = 3

print( '{} + {} = {}'.format(a, b, a+b))
print( '{} - {} = {}'.format(a, b, a-b))
print( '{} * {} = {}'.format(a, b, a*b))


radius = 10
pi = 3.14
area = pi * radius ** 2

formatted_string = 'The area of a circle with a readius {} is {:.2f}'.format(radius, area)
print(formatted_string)

name = 'Ginura'
lst = 'Amarase'

full = 'My name is {} {}' .format(name, lst)
print(full)