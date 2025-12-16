# this function converts string --> to a list of floats
def parse_number(raw:str) -> list[float]: #takes string as input and then output a list of floats
    numbers: list[float] = [] 
    for part in raw.split(","): #raw.split() delivers a list of items which were separated by a comma
        part = part.strip() #then this will delete any whitespaces front and back
        if not part: #the empty strings ("") or ",," will be skipped
            continue 
        numbers.append(float(part)) #anything that is wrong, non empty entries throws the value error
    return numbers

#talk to user and retry on invalid input
def prompt_numbers(prompt:str) -> list[float]:
    while True:
        raw = input(prompt) #what everthe input given is stored inside the raw variable 
        try:
            return parse_number(raw) #then we convert the string to list of floats
        except ValueError as e:
            print(e)

def add_nums(values: list[float]) -> float:
    return sum(values) #this sum is a built in python function

def sub(values: list[float]) -> float:
    result = values[0]
    for value in values[1:]:
        result -= value
    return result

def mul(values: list[float]) -> float:
    result = values[0]
    for value in values[1:]:
        result = result * value
    return result

def div(values: list[float]) -> float:
    result = values[0] / values[1]
    return result
    
# print(reduce(operator.sub, (3,4))) #output --> -1 means 3 - 4

operations_lst = ["ADD", "SUBTRACT", "MULTIPLY", "DIVISION"]
def print_option_menu(operations_lst):
    print("<-----MENU--------->")
    for index, i in enumerate(operations_lst):
        print(f" {index+1}: {i}")
    print("<------------------>")

def chosen_option(chosen_user_op):
    return operations_lst[chosen_user_op-1]

def choosing_ops(menu_items: str) -> int:
    while True:
        option = int(input(menu_items))
        try:
            choice = option
        except ValueError as error:
            # print(error)
            print("The input must be a number (e.g. 1, 2, 3, 4)")
        
        if choice not in range(1,len(operations_lst)+1):
            print(f"Please choose a number between 1 and {len(operations_lst)}.")
            continue
        return choice

def choosing_the_operation(user_option):
    entered_nums = prompt_numbers("Enter the values:")
    total = 0
    if user_option == 1:
        total = add_nums(entered_nums)
        print(f"SUM:{total}")
    elif user_option == 2:
        subtract_result = sub(entered_nums)
        print(f"SUB:{subtract_result}")
    elif user_option == 3:
        multiplied_result = mul(entered_nums)
        print(f"MUL:{multiplied_result}")
    elif user_option == 4:
        division_result = div(entered_nums)
        print(f"DIV:{division_result}")

def main():
    print_option_menu(operations_lst)
    num_chose = choosing_ops("Enter the Option You Seek:")
    user_option_chosed = chosen_option(num_chose)
    print(f"You chose: {user_option_chosed}")

    choosing_the_operation(num_chose)
    
if __name__ == "__main__":
    main()