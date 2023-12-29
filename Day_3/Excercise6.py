from tkinter import SE


Years = int(input('Number of Years You Lived:'))
Seconds_in_a_Hour = 60 * 60
Seconds_in_a_Day = Seconds_in_a_Hour * 24
Seconds_in_a_year = Seconds_in_a_Day * 365 

print('You Have Lived:', Seconds_in_a_year * Years, 'S')