# class Dog:

#     def bark(self):
#         print('bark')
        
#     def add_one(self, x):
#         return x + 1

#     def range_of(self, y):
#         for i in range(0, y):
#             print(i)

# range_1 = Dog()
# range_1.range_of(10)

# range_2 = Dog()
# range_2.range_of(8)

# num = Dog()
# print(num.add_one(5))

# d = Dog()
# d.bark()

class Dog:

    def __init__(self, name, age): 
        self.name1 = name
        self.age1 = age
        # print(name)
    
    def get_name(self):
        return self.name1
    
    def get_age(self):
        return self.age1

d = Dog('Tim', 30)
print(d.get_name())

d1 = Dog('Bill', 40)
print(d1.get_name())

print(d.get_age() + d1.get_age())