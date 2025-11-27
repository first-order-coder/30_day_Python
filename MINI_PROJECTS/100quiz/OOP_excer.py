# class Vehicle:
#     #class attribute
#     color = 'white'
#     def __init__(self, name, max_speed, mileage, capacity):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.capacity = capacity
    
#     def seating_capacity(self, capacity):
#         self.capacity = capacity
#         return f'the Seating capacity of {self.name} is {capacity} passengers'
    
#     def fare(self):
#         return self.capacity * 100
    
# class Bus(Vehicle):
    
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount

# School_Bus = Bus('volvo', 120, 90, 50)
# print(School_Bus.fare())
import re
regex = r'[a-zA-Z]'
pattern = re.findall(regex,'ABd1234@1')

print(pattern)