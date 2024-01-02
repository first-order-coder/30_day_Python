

st_dct = {
   'first name': 'Ginura', 
   'Last name': 'Amarasena', 
   'Gender': 'Male', 
   'Skills': 'Programming',
   'Address': {
               'House': '2',
               'Road': 'Ruwanwella'
              }
          }

print(st_dct['first name'])
st_dct['Address1'] = 'Avenue'
print(st_dct)

keys = st_dct.keys()
values = st_dct.values() 

print(f'Keys:{st_dct.keys()}\nValues:{values}')
# for i in st_dct:
#    print(i['first name'], i['Last name'])

# print(st_dct['Skills'])
# print(type(st_dct['Skills']))

# st_dct['Skills'] = 'Music'
# print(st_dct)

# print(st_dct.items())

# number = int(input('Number of Rows:'))
# # for i in range (number + 1):
# #    for j in range (number + 1):
# #       print('#', end='')
# #    print('')

# for i in range(number + 1):
#    for j in range(i + 1): 
#       print('#', end=' ')
#    print()