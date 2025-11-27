import string
import random

# user_input = input('Type A Number:')

# if user_input.isdigit():
#     user_input = int(user_input)

#     if user_input <= 0:
#         print("Enter A nmber bigger than zero next time")
#         quit()
# else:
#     print('Please Enter A Number Next Time')
#     quit()

# random_number = random.randint(0, user_input)
# print(random_number)

guess = 0
while True:
    
    guess += 1
    user_guess = input('Make A Guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please Enter A Number Next Time')
        continue
    
    random_number = random.randint(0, user_guess)
    if user_guess == random_number:
        print('You Got It')
        break
    elif user_guess > random_number:
            print('you were above the number')
    else:
            print('you were below the number')
            
    print('you go it in', guess, 'guesses')