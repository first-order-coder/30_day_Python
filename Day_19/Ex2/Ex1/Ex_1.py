# def write_txt():
#     f = open(r'C:\Users\ginuram\Desktop\Dekstop\\30DaysofPython\Day_19\example.txt', 'a')
#     f.write('This is an example to show how to open a file and read.This is the second line of the text.')
#     f.close()

# write_txt()

# def print_1():
#     f = open(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\Day_19\example.txt', 'r')
#     txt = f.read(10)
#     print(txt)
# print_1()

# def split():
#     f = open(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\Day_19\example.txt', 'r')
#     lines = f.read().splitlines()
#     print(lines)
#     f.close()
# split()

def open_1():
    with open(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\Day_19\example1.txt', 'w') as f:
        f.write('''After we open a file, we should close it. There is a high tendency of forgetting to close them. 
                    There is a new way of opening files using with - 
                    closes the files by itself. Let us rewrite the the previous example with the with method:''')
        f.splitlines()
open_1()

