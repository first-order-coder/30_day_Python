# class Vehicle:

#     #class Attribute
#     color = 'white'

#     def __init__(self, name, max_speed, mileage,):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
    
#     def infor(self):
#         print(f'Color: {Vehicle.color} Name: {self.name} Max Speed: {self.max_speed} Mileage: {self.mileage}')

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# bus = Bus('Volvo', 120, 12)
# bus.infor()

# car = Car('Audi', 130, 15)
# car.infor()



# class Dog(object):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("Hi I'm", self.name, "And I'm", self.age)

#     def change_age(self, age):
#         self.age = age

# tim = Dog('Tim', 55)
# fred = Dog('Fred', 4)
# fred.change_age(10)
# tim.change_age(15)
# tim.speak()
# fred.speak()

class Dog:

    def __init__(self, name, age):
        self.name = name #instance variable aka attribute
        self.age = age
    
    def speak(self):
        print(f'Hi my name is {self.name}')
        

Tim = Dog('TIM', 22)
JOhn = Dog('GOADS', 23)

Tim.speak()
JOhn.speak()

class Cat(Dog):

    def __init__(self, name, age, color):
        self.color = color
        super.__init__(name, age)
    




















