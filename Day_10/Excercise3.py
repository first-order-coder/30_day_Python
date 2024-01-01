# rows = 5
# for i in range(1, 1 + rows):
#     for j in range(1, 1 + i):
#         print("#", end=' ')
#     print()

# rows = 5
# for i  in range(1, 6):
#     for j in range(1, 4):
#         print( '*', end='')
#     print()

# first = [2 ,4 ,6]
# second = [2, 4, 6]
# for i in first:
#     for j in second:
#       if i == j:
#          continue
#       print(i, '*', j, '=', i * j)


for i in range(4):
    for j in range(4):
        if i == j:
            break
        print( i, j)

# for i in range(1, 6):
#     for j in range(1,4):
#         print('*', end=' ')
#     print()

