editing = True

class Student:

    _class = "Student"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        

John = Student("John", 21)
Jane = Student("Jane", 22)
Jeff = Student("Jeff", 23)

print(getattr(John, "class_"))