READ_PERMISSION = 4
WRITE_PERMISSION = 3
EXECUTE_PERMISSION = 1

user_Permissions = 6

if (user_Permissions & READ_PERMISSION) == READ_PERMISSION:
    print('Can Read')

else:
    print('Cannot Read')

print(user_Permissions & READ_PERMISSION)