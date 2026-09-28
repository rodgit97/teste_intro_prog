#variaveis de classe

class Student:

    class_year = 2024
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1


student1 = Student("rod", 18)
student2 = Student("jack", 22)

student3 = Student("patricio",23)
student4 = Student("Areia",55)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print()
print(student1.class_year)
print(student2.class_year)
print()
print(Student.num_student)

print()
print(f"minha gradulacao de classe de {Student.class_year} era {Student.num_student} estudantes")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

