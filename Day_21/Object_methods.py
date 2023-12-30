# class Person:
#     def __init__ (self, firstname, lastname, age, country, city):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city

# p = Person('Ginura', 'Amarasena', 25, 'Finland', 'Helsinki')
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.city)
 
'''p = Person() is creating a object in Person class by calling the class then the values are inserted to P object. 
    Which will execute in init function using its parameters.  '''

# class Person:
#     def __init__ (self, firstname, lastname, age, country, city):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city
#     def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

# p =Person('Asabeneh', 'Yetayeh', 25, 'Finland', 'Helsinki')
# print(p.person_info())

# # class Geek:
#     #default constructor
#     def __init__(self):
#         self.geek = 'GeeksforGeeks'
#     def print_Geek(self):
#         print(self.geek)

# obj1 = Geek()

# obj1.print_Geek()


class Vehicle:
    name = "tesla" #class variable

    def __init__(self, price, gas, color):
        self.price_1 = price   #instance variable
        self.gas = gas        #instance variable
        self.color = color     #instance variable

    '''class methods cant access instance variables:: but it can access class variables'''

    # @classmethod 
    # def see(cls):   print(cls.gas) >> AttributeError: type object 'Car' has no attribute 'gas' 
    #     print(cls.gas)
    #     print(cls.name)
    
    def filluptank(self):
        self.gas = 100
    
    def emptygas(self):
        self.gas = 0
    
    def gaslef(self):
        print(self.gas)

class Car(Vehicle):
    def __init__(self,price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed
    
    def beep(self):
        print('Beep Beep')

class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
    
    def beep(self):
        print('Honk Honk') 



tesla = Car(13500, 60, 'red', 130)
# tesla.see()
# print(tesla.speed + tesla.price)
tesla.beep()

# def factor(x):
#     return x ** 2
# print(factor(10))
#     print(x ** 2)
# factor(10)            THEY BOTH WORK IN FUNCTIONS
