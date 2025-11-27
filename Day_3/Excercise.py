def read_float(prompt: str) -> float: #function will return a float, will take a string, type hint: prompt should should be a string (prompt, type_=str) --> (text shown to user)
    while True:
        try:
            user_input = float(input(prompt))
        except ValueError: #ValueError exception occurs if a function recives a value of wrong type
            print("Please enter a valid number")
        else:
            break
    return user_input

def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

def triangle_perimeter(a:float, b:float, c:float) -> float:
    return a+b+c

def main() -> None: #returns None
    age:int = 10
    height:float = 5.9
    velocity:complex = 1 + 1j

    #area from base and height
    base = read_float("Enter base: ")
    tri_height = read_float("Enter height: ") # handling of the input is given to read_float funciton 
    area = triangle_area(base, tri_height)
    print(f"Area of the triangle is: {area}")

    #perimeter of the triangle
    side_a = read_float("Enter side a: ")
    side_b = read_float("Enter side b: ")
    side_c = read_float("Enter side c: ")
    perimeter = triangle_perimeter(side_a, side_b, side_c)
    print(f"Perimeter of the triangle is {perimeter} m")

if __name__ == "__main__": #name guard
    main()