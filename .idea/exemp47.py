#inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    """def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")"""
    def speak(self):
        print(f"au")
    #pass

class Cat(Animal):
    def speak(self):
        print(f"miau")
    """def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")"""

    #pass

class Mouse(Animal):
    def speak(self):
        print(f"i")
    """def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")"""

    #pass

dog = Dog("Pintinhas")
cat = Cat("Tareco")
mouse = Mouse("Guinchinho")

print(dog.name)
print(dog.is_alive)
print(dog.eat())
print(dog.sleep())

print(cat.name)
print(cat.is_alive)
print(cat.eat())
print(cat.sleep())

print(mouse.name)
print(mouse.is_alive)
print(mouse.eat())
print(mouse.sleep())

print()
dog.speak()
cat.speak()
mouse.speak()