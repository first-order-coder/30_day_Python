# text = 'Maths'
# # print(f'{text:_>200} {text:_<200}')
# print(f'{text:_^150}')

class Vehicle:
        
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage


# model_x = Vehicle('Texsle',300, 450)

class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage, capacity):
                    self.capacity = capacity
                    super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self):
            print(f'The seating capacity of {self.name} is {self.capacity} passengers')

    def print_bus(self):
        print(f'Vehicle: {self.name} Max Speed: {self.max_speed} Mileage: {self.mileage}')

bus = Bus('Volvo', 80, 120, 50)
bus.print_bus()

bus.seating_capacity()