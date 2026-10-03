#polimorfismo
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    #pass
    def area(self):
        return 3.14* self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    #pass
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    #pass
    def area(self):
        return self.base * self.height * 0.5

class Pizza():
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes=[Circle(4),Square(5),Triangle(6,7),Pizza("presunto",15)]

for shape in shapes:
    print(shape.area())
    print(f"{shape.area()} cm")