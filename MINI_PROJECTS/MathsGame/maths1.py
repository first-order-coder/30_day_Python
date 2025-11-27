print(f"{'WLECOME TO MATHS':_>20}")

start = 'S'
quit = 'Q'


qustion1 = input(f'Press S to Start and Q to Quit: ')
if qustion1 == start.lower():
    print('Get Ready')

elif qustion1 == quit:
    print('Bye See You Later')
    quit
else:
    print('S or Q only')


while True:
    question2 = input('What is 1 + 1 = ')
    if question2.isdigit():
        question2 = int(question2)
    else:
        print('Please Enter A Number Next Time')
        continue

    if question2 == 2:
        print('You Got It Correct')
        break
    else:
        print('Wrong, Tryagain')
        

while True:
    question3 = input('What is 2 + 2 = ')
    if question3.isdigit():
        question3 = int(question3)
    else:
        print('Please Enter A Number Next Time')
        continue
    
    if question3 == 4:
        print('You Got It Correct')
        break
    else:
        print('Wrong, Tryagain')
        


