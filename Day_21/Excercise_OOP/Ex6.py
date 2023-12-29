class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def print__(self):
        print(self.name, self.mileage)    

    def fare(self):
        return self.capacity * 100

#method overriding

class Bus(Vehicle):
    # def fare(self):
    #     amount = super().fare() #using super function to bring fare function in parent class without changing the parent class attribute
    #     amount += amount * 10 / 100
    #     print(f'Toatal Bus Fare is {amount}')

    def __init__(self, name, mileage, capacity):
        self.capacity = capacity
        super().__init__(name, mileage)
        print(name, mileage)
        
b = Vehicle('Tim', 120)
b.print__()

bus = Bus('Volvo', 120, 50)
print(bus.fare())