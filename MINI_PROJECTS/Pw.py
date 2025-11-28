import random
import string
import pyautogui


number = int(pyautogui.password('Enter Number OF IDS:'))
chars = int(pyautogui.password('Enter Number Of Chars:'))

for _ in range(0, number):
    result = ''.join(random.choices(string.ascii_letters + string.digits, k= chars))
    print(result)

number_of_ID = 0
while number_of_ID < number:
    result1 =''.join(random.choices(string.digits + string.ascii_uppercase, k =chars))
    number_of_ID = number_of_ID + 1
    print(result1)


count = 0
while True:
    result1 =''.join(random.choices(string.digits + string.ascii_uppercase, k =chars))
    result2 =''.join(random.choices(string.digits + string.ascii_uppercase, k =chars))
    count += 1
    if result1 == result2:
        print(result1, result2)
        
        break
    else:
        print(result1, result2)
        
        print('It took', count, 'lines to get')
        
    continue
