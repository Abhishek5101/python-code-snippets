class Vehicle:
    def __init__(self, name):
        self.name = name
        print("The name of the vehicle is {}".format(name))

    def top_speed(self):
        print("The top speed for {} is 180MPH".format(self.name))


class Car(Vehicle):
    def __init__(self):
        super().__init__('ford')
        super().top_speed()


v = Vehicle('Jeep')
g = Car()

