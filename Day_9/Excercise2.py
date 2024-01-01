marks = int(input('Enter the Students Mark:'))

if 80 < marks <= 100:
    print('The Grade Is A')

elif 75 < marks <= 89:
    print('The Grade Is B')

elif 60 < marks <= 69:
    print('The Grade Is C')

elif 50 < marks <= 59:
    print('The Grade Is D')

else:
    print('The Grade Is F')