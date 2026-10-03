# metodos de classes

class Student:

    count=0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa

# metodo de instancia:
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"numero total de estudantes:{cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            #return f"{cls.total_gpa/cls.count}"
            return f"average gpa {cls.total_gpa/cls.count:.2f}"

student1 = Student("bob", 3.2)
student2 = Student("patricio", 2.0)
student3 = Student("sandra", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())
print("-----------------------")
class Student:


    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa


# metodo de instancia:

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self,other):
        return self.name == other.name

    def __gt__(self,other):
        return self.gpa > other.gpa

student1 = Student("bob", 3.2)
student2 = Student("patricio", 2.0)
student3 = Student("sandra", 4.0)

print(student1)
print(student1 == student2)
print(student1 > student2)

print("-----------------------")



