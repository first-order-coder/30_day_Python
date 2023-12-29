import re
from tabnanny import check
#make a regular expression

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b'
def is_valid_variable(email):

    if(re.fullmatch(regex, email)):
        print('Valid Email')
    
    else:
        print('Invalid Email')

if __name__ == '__main__':

    email = "ginura@gmail.com"
    
    is_valid_variable(email)

    email = 'out__2@bmailcom'
    
    is_valid_variable(email)
