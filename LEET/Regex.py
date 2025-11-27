import re

with open(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\LEET\ship.text') as f:
    s = f.read()

pattern = '\d+'
match = re.findall(pattern, s)
print(match)