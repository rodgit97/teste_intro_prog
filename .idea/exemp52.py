#static methods ⚡

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager","cashier","cook","janitor"]
        return position in valid_position

employee1 = Employee("Eugenio", "Manager")
employee2 = Employee("lula", "cashier")
employee3 = Employee("bob", "cook")

print(employee1.get_info())

print(Employee.is_valid_position("cook"))
print(Employee.is_valid_position("coisa"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

