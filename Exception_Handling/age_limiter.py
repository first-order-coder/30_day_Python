class InvalidAgeError(ValueError):
    def __init__(self, message:str, value:int ) -> None:
        super().__init__(message)
        self.value = value 

def parse_age(raw: str) -> int: #every function must return something in this case it returns int(of input value)
    raw = raw.strip()
    if not raw:
        raise InvalidAgeError(message="Age cannot be empty", value=100)
    if not raw.isdigit():
        raise InvalidAgeError(message="Age must be a digit", value=101)
    age = int(raw)
    if not (0 <= age <= 130):
        raise InvalidAgeError(message="Age must be between 0 and 130", value=102)
    return age

while True:
    try:
        age = parse_age(input("Enter Age: "))
        print(f"Valid age: {age}")
        break
    except InvalidAgeError as e:
        print(f'Invalid Input: Error Code:{e.value} --> {e} ')

#test