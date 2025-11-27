import re
import random
import string

password_count = int(input('Number of Passwords Suggested:>'))
number_of_characters = int(input('Enter Number Of Characters:>'))

value = []
for _ in range(0, password_count + 1):
    suggested_password =''.join(random.choices(string.ascii_letters + string.digits, k= number_of_characters)) 
    lst = re.split(' ', suggested_password)
    value += lst
    # print(value)
    print(suggested_password)


password = input('Enter Password:>')

while True:
    user_name = input('Enter User Name:>')
    if user_name == '':
        print('USer name cannot be none, Try Again')
    
    else:
        print('Login successful')
        with open(r'C:\Users\ginuram\Desktop\password.txt', 'a') as f:
            f.write(f'\nUsername = {user_name}\nPassword = {password}')
        break

