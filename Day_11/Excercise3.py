# def is_prime(num):
#     if num > 1:
#         for i in range(2, int(num/2)+1):
#             if (num % i) == 0:
#                 print(num, "is not a prime number")
#                 break
#         else:
#             print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")
# print(is_prime(11))

def same_data_type():
    list = ['Monday', 'Sunday', 'Tuesday', 'Wednesday', 4]
    if(type(set(list)) == type(list)):
        print('They are same')
    else:
        print('They are not the same')
same_data_type()

