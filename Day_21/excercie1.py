class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Whaever')

class Dog(Pet):

    def declare_att(self,color):
        self.color = color

    def speak(self):
        print('Bark')
    
    def get_age(self):
        return self.age

class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color} color.')


    def speak(self):
        print('Meow')
    
    def get_age(self):
        return self.age

p = Pet('Shefy', 14)
p.speak()

d = Dog('Dora', 22)
d.speak()
print(d.get_age())

c = Cat('Kalu', 23, 'black')
c.show()

# x = 10
# print(complex(x))

# txt = 'Hello'
# txt = txt.upper()
# txt1 = txt.isupper()

# print(txt, txt1)
# print(txt.replace('H', 'j'))

# age = 112
# t = 'Hello my name and I am {} '
# print(t.format(age))

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car['model'])
# print(car.get('model'))

# while True:
#     for i in range(8):
#         mountain_h = int(input())  # represents the height of one mountain.

#     # Write an action using print
#     # To debug: print("Debug messages...", file=sys.stderr, flush=True)

#     # The index of the mountain to fire on.
#     print("3")

# def fizzBuzz(n):
#     for i in range(1, n+1):
#         if i % 15 == 0:
#             print('FizzBuzz')
        
#         elif i % 3 == 0 and i % 5 != 0:
#             print('Fizz')
        
#         elif i % 5 == 0 and i % 3 != 0:
#             print('Buzz')
        
#         else:
#             print(i)
# fizzBuzz(65)

#stop using print when runing functions 
