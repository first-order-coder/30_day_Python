# from functools import lru_cache
# import random
# import string

# char = int(input('Enter Chars:'))
# id = int(input('Enter Number of ID:'))
# for _ in range(char + 1):
#     format =''.join(random.choices(string.ascii_letters + string.digits, k = char))
#     print(format)

# while True:
#     n = int(input('Whats N:'))
#     if n > 0:
#         break

# for _ in range(n):
#     print("MEOW")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input('Whats N:'))
        if n > 0:
            break
    return(n)

def meow(n):
    for _ in range(n):
        print('meow')

main()