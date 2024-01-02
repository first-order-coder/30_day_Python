first_name = 'Ginura'
last_name = 'Amarasena'

language = 'Python'

formatted_string = 'My full name is %s and I learn %s' %(first_name + ' ' + last_name, language)
print(formatted_string)


radius = 10
pi = 3.14
area = pi * radius **2

formatted_string2 = 'Area of a circle with radius %d is %.2f.' %(radius, area)
print(formatted_string2)

python_libraries = ['Django', 'Ginura', 'World', 'Health']


formatted_string3 = 'Libraries of python are: %s' %(python_libraries)
print(formatted_string3)

names = 'Ginura'
lst_name = 'Amarase'

full = 'My name is %s' %(names + ' ' + lst_name)
print(full)

names = 'Ginura'
lst_name = 'Amarase'

full1 = f'my name is {names + " " + last_name} annd i m 20 ears oldfft'
print(full1)