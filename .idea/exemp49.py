#super()

#classe Pai:
#pass
#classe Criaca(Pai):
#pass
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        #self.color = color
        #self.filled = filled
        #self.filled = is_filled
        self.radius = radius
    #pass

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        #self.color = color
        #self.filled = is_filled
        self.width = width
    #pass

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        #self.color = color
        #self.filled = is_filled
        self.width = width
        self.height = height
    #pass

circle = Circle(color="red", is_filled=True, radius=5)
square = Square("green", False, 6)
triangle = Triangle("yellow", False, 7,8)
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius} cm")
print()
print(square.color)
print(square.is_filled)
print(f"{square.width} cm")
print()
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width} cm")
print(f"{triangle.height} cm")

print("---------------------------------------")

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} filled {'filled ' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)

        #self.color = color
        #self.filled = filled
        #self.filled = is_filled
        self.radius = radius
    #pass
    def describe(self):
        super().describe()
        print(f"é um circulo com a area de {3.14 * self.radius * self.radius} cm^2 ")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        #self.color = color
        #self.filled = is_filled
        self.width = width


    #pass
    def describe(self):
        super().describe()
        print(f"é um quadrado com a area de { self.width * self.width} cm^2 ")
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        #self.color = color
        #self.filled = is_filled
        self.width = width
        self.height = height
    #pass
    def describe(self):
        super().describe()
        print(f"é um triangulo com a area de {self.width * self.height/2} cm^2 ")

circle = Circle(color="red", is_filled=True, radius=5)
square = Square("green", False, 6)
triangle = Triangle("yellow", False, 7,8)

circle.describe()
square.describe()
triangle.describe()


print("---------------------------------------")