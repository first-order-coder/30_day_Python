from re import sub


challenge = 'thirty days of python'
sub_string = 'hi'

print(challenge.index(sub_string))

print(challenge.rindex(sub_string))

challenge = 'thirty days of python'

print(challenge.isalnum())

challenge_1 = 'thirtydaysofpython'
challenge_2 = '30daysofpython'

print(challenge_1.isalnum() , challenge_2.isalnum())

print(challenge.isalpha())
print(challenge_1.isalpha())
print(challenge_2.isalpha())

num = '123'
num_1 = '12.33'

print(num.isdecimal())
print(num_1.isdecimal())

