age = int(input('Enter Your Age:'))

if age >= 18:
    print('You are old enough to drive')
elif age < 18:
    need_to_wait = (18 - age)
    print('You are not old enough to drive so you need to stay', need_to_wait ,'years to drive')
