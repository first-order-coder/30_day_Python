# import random
# import string

# def id_generator(length):
#     letters = string.ascii_lowercase
#     result_str = ' '.join(random.choice(letters) for i in range(length))
#     print("random string of length:", length, " is", result_str)
# print(id_generator(10))

# # print(string.ascii_uppercase)
# # print(string.digits)
# # print(string.ascii_uppercase + string.digits)

# # mylist = ['Banana', 'Cherry', 'Apple']
# # print(random.choices(mylist, weights= [10, 1, 1], k = 14))

# # s =7
# # print(''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_letters, k =s)))
import string
import random

def user_id_gen_by_user():
    number_of_chracters = int(input('Enter Chars:'))
    number_of_IDS = int(input("Enter Number Of IDs:"))
    for _ in range(number_of_IDS ):
        run = ''.join(random.choices(string.ascii_letters + string.digits, k = number_of_chracters))   
        print(run)
user_id_gen_by_user()

# def rgb_color_gen():
#     color_1 = range(0, 255)
#     run = random.choices(color_1, k = 3)
#     print(run)
# rgb_color_gen()






