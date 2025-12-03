from cryptography.fernet import Fernet

def load_key():
    file = open('./MINI_PROJECTS/PW1/key.key', 'rb')
    key = file.read()
    file.close()
    return key

master_password = input('What is your password:')
key = load_key() + master_password.encode()
fer = Fernet(key)

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''

def update():
    with open('passwords.txt') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pawd = data.split(' | ')
            print('USER:', user, '|', 'Password:', fer.decrypt(pawd.encode()).decode())
        

def create():
    name = input('Account Name:')
    pwd = input('Create Password:')

    with open('./MINI_PROJECTS/PW1/passwords.txt', 'a') as f:
        f.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input('To Create or Update passwords Type(C / U).  To Quit Type( Q )>>:>>').lower()
    if mode == 'q':
        break
    
    if mode == 'u':
        update()
    
    elif mode == 'c':
        create()
    
    else:
        print('Invalid Mode.')
        continue