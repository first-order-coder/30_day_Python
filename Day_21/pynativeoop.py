# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):

#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)

#     def display(self):
#         print(f'Vehicle Name :{self.name} Speed: {self.max_speed} Milage: {self.mileage}')

# b1 = Bus('Volvo', 180, 1000)

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):
    
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

b1 = Bus('Volvo', 180, 1000)

print(b1.seating_capacity())
