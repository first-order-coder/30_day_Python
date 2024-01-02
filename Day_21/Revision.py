class Pet:
    def __init__(self, name, age, legs): #constructor method, __init__ is execuetde automatically and immediately once a object is created.
        self.name = name #attribute
        self.age_1 = age
        self.legs = legs
        # print(legs) this will be executed whenever we create an just and obeject 
    
    def get_legs(self):
        print("has", self.legs , 'Legs')
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age_1

    def speak(self):
        print('Dog of the Year is', self.name , self.age_1)

"Why do we use inheritance? we dont have to copy all the attributes, functions and methods used in Pet class"    
class Dog(Pet): #now this Dog class is inherited from pet class all the attributes

    def set_age(self,age):
        self.age_1 = age #we can set a new attribute value

    def speak(self):
        print('Bark')

class Pigeon(Pet):
    def speak(self):
        print('Bow Bow')

# class Cat(Pet):


Dog_1 = Dog('Gus', 5, 4)
print(Dog_1.get_age())
Dog_1.set_age(23)
print(Dog_1.get_age())

# print(Dog_1.get_name())
# Dog_1.speak()
# Dog_1.get_legs()

# Pigeon_1 = Pigeon('Alan', 4, 2)
# print(f'\n{Pigeon_1.get_name()}')
# Pigeon_1.speak()
# Pigeon_1.get_legs()
# print(Pet_1.get_age()) this doesnt work >> 'Pet' object has no attribute 'get_age'<<




# >> Creating a object list out of name list <<

# names = '''Buddy
# Tucker
# Jack
# Leo
# Duke
# Winston
# Bear
# Teddy
# Loki
# Archie
# Joey
# Oliver
# Beau
# Murphey
# Jax
# Gunther
# Bentley
# Finn
# Ace
# Scout
# Ross
# Louie
# Gus
# Moose
# Hank
# Bruno
# Ollie
# Lucky
# Thor
# Chandler
# Kobe
# Bandit'''

# lst_names = names.split()

# for count, dog_name in enumerate(lst_names):
#     # print(f'd{count}= Dog({dog_name})')
#     count = Pet(dog_name, count)
#     count.speak()
    