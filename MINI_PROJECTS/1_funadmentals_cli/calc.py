from functools import reduce
import operator

# this function converts string --> to a list of floats
def parse_number(raw:str) -> list[float]: #takes string as input and then output a list of floats
    numbers: list[float] = [] 
    for part in raw.split(","): #raw.split() delivers a list of items which were separated by a comma
        part = part.strip() #then this will delete any whitespaces front and back
        if not part:
            continue #anything thats not a part will skip
        numbers.append(float(part)) 
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

# def subtract_nums(values: list[float]) -> float:
#     return 

print(reduce(operator.sub, (3,4))) #output --> -1 means 3 - 4


def main():
    entered_nums = prompt_numbers("Enter the values:")
    total = add_nums(entered_nums)
    print(f"SUM:{total}")

if __name__ == "__main__":
    main()