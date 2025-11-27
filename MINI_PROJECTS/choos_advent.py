from asyncore import read


name = input('Enter Your Name Adventurer:')
print(f'Welcome {name} to this adventure!')

def ready():
    ready = input('Are you ready for the Adventure (Y / N) :) ')
    ready = ready.lower()
    if ready == 'y':
        print('Welcome To Jumanji')
    elif ready == 'n':
        print('You Are Not Ready Yet')
        quit()
    else:
        print('Enter Only Y or N')

    print('Hey')

ready()
