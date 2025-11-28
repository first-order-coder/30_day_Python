

number_of_ID = 0
while number_of_ID < number:
    result1 =''.join(random.choices(string.digits + string.ascii_uppercase, k =chars))
    number_of_ID = number_of_ID + 1
    print(result1)


count = 0
while True:
    result1 =''.join(random.choices(string.digits + string.ascii_uppercase, k =2))
    result2 =''.join(random.choices(string.digits + string.ascii_uppercase, k =2))
    count += 1
    if result1 == result2:
        print(result1, result2)
        
        break
    else:
        print(result1, result2)
        
        print('It took', count, 'lines to get')
        
    continue
