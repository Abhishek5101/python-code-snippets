class Vehicle:
    def __init__(self, name):
        self.name = name
        print("The name of the vehicle is {}".format(name))


class Car(Vehicle):
    def __init__(self):
        super().__init__('ford')


v = Vehicle('Jeep')
g = Car()

