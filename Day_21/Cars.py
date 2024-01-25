class Car:
    def __init__(self, speed, time, color):
        self.speed = speed
        self.time = time
        self.color = color

    def get_color(self):
        print(self.color)
    
    def get_speed(self):
        print(self.speed)

    def distance_travelled(self):
        distance = self.speed * self.time
        print(distance, "m")
    
car_1 = Car(25, 30, 'red')
car_2 = Car(35, 10, 'green')
car_3 = Car(45, 20, 'blue')
car_4 = Car(15, 90, 'blcak')
car_5 = Car(35, 20, 'orange')

car_5.get_speed()
car_5.get_color()
car_5.distance_travelled()