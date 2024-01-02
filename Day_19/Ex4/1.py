import re

regex_pattern = r'[A-Za-z0-9]+@[A-Za-z0-9.-]+.[A-Za-z0-9]{1,}'
def email_extract():
    with open(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\Day_19\Ex4\list.txt', 'r') as f:
        matches = re.findall(regex_pattern, f.read())
        print(matches)
email_extract()