#multiple inhertance
class Animal:
    def __init__(self, name):
        self.name = name
    #----------------------
    def eat(self):
        print(f"este {self.name} está comendo")

    def sleep(self):
        print(f"este {self.name}  está a dormir")
    #pass

class Prey(Animal):
    def flee(self):
        print(f"este {self.name}  está escapar")
    #pass
class Predator(Animal):
    def hunt(self):
        print(f"este {self.name}  está a caçar")
    #pass

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

"""rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
fish.hunt()
hawk.hunt()
print()"""
"""rabbit = Rabbit("bigodes")
fish = Fish("bolhas")
hawk = Hawk("bico")"""
print()

#rabbit.flee()

print()
"""rabbit.eat()
fish.sleep()"""

rabbit = Rabbit("bigodes")
fish = Fish("bolhas")
hawk = Hawk("bico")

rabbit.eat()
fish.sleep()
hawk.hunt()

