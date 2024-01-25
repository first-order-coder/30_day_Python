print(chr(65)) #will printout symbol for ASCII numbering system
print(complex(3,4)) #(3+4j) output complex number

dict_1 = {'Name': 'Bagginns', 'Address': 'Baghill', 'Age': 55}
print(dict_1.keys())
print(dict_1['Address'])

quotient, remainder = divmod(10, 3)
print(quotient, remainder) #3 1

''' Will Evaluate a string as a Python Function '''
x = 'print(5)' #will evaluate a string as a python Function
eval(x)

y = 'print(dict_1.keys())' 
eval(y)

lst = ['a', 'b', 'c']
print(lst)
code = eval(input('What ever your enter eval will find it:> ')) #if i enter "lst.remove('a')" as a input then it will be excuted.
print(lst) 

''' ^^^ VERY DANGEROUS TO USE IN INPUT ^^^'''

