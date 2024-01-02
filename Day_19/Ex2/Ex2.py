# def obama_1():
#     with open (r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\Day_19\Ex2\obama.txt', 'r') as f:
#         lines = f.read()
#         nlines = lines.split('.')
#         print(f'Number of Lines are: {len(nlines)}')

#         n1 = lines.split( )
#         print(len(n1))
# obama_1()

from datetime import datetime

current = datetime.now()
time = (str(current.time())[0:8]).replace(':', '-')

# name = current.date() + time
print(time)
# print(name)