import random

user_wins = 0
computer_wins = 0


user_input_1 = input("Enter 'S' to start the game or 'Q' to Quit: ")    
user_input_1 = user_input_1.lower()
if user_input_1 == 's':
        print('\n ****** ⚙️   ✂️   📄  Welcome To Rock Paper Scissor Game 📄   ✂️   ⚙️ *******')


elif user_input_1 == 'q':
        print('See U Next Time :)')
        quit()
else:
        print('Enter only "S" or "Q"')
        quit()

while True:  
    user_input_2 = input('\nRock? Paper? Scossor?:')
    user_input_2 = user_input_2.lower()
    
    items = ['Rock', 'Paper', 'Scissor']
    for i in range(len(items)):
        items[i] = items[i].lower()
    
    computer_gen = random.choice(items)
   
    if user_input_2 == 'rock' and computer_gen == 'Scissor':
        print('You got it')
        continue

    if user_input_2 == 'rock' and computer_gen == 'Paper':
        print('You lost it')
        continue 

    if user_input_2 == 'paper' and computer_gen == 'Scissor':
        print('You lost it')
        continue

    if user_input_2 == 'paper' and computer_gen == 'Rock':
        print('You got it')
        continue
    
    if user_input_2 == 'scissor' and computer_gen == 'Rock':
        print('You lost it')
        continue
    
    if user_input_2 == 'scissor' and computer_gen == 'Paper':
        print('You got it')
        continue
    
    else:
        print('Try Again')
        continue