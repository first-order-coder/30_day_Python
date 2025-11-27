from datetime import datetime

year_1 = int(input('Enter a Year 1: '))
month_1 = int(input('Enter Month 1: '))
day_1 = int(input('Enter Day 1: '))

date_1 = datetime(year_1, month_1, day_1)

year_2= int(input('Enter Year 2: '))
month_2 = int(input('Enter Month 2: '))
day_2 = int(input('Enter Day 2: '))

date_2 = datetime(year_2, month_2, day_2)

difference = date_2 - date_1
datetime_1 = datetime(difference)
print(datetime_1)