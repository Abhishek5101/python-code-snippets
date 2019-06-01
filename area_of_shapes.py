class AreaOfRectangle:
    def __init__(self, length, width):
        self.len = length
        self.wid = width
        self.area = length * width
        print(self.area)


class AreaOfCircle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2

    def area(self):
        return 3.14 * self.radius * self.radius


cir1 = AreaOfCircle(6)
print(cir1.area())
