my_age = 21
your_age = int(input('Enter Your Age:'))

if my_age > your_age:
    difference = abs( my_age - your_age)
    if difference == 1:
        print('You are', difference ,'year younger than me')
    else:
        print('You are', difference ,'years younger than me')

elif my_age < your_age:
    difference = abs( my_age - your_age)
    if difference == 1:
        print('You are', difference ,'year Older than me')
    else:
        print('You are', difference ,'years Older than me')