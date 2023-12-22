class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, college, classroom):
        super().__init__(name, age, gender)
        self.college = college
        self.classroom = classroom

    def personInfo(self):
        return f"{super().personInfo()}, College: {self.college}, Class: {self.classroom}"

class Teacher(Person):
    def __init__(self, name, age, gender, college, profession):
        super().__init__(name, age, gender)
        self.college = college
        self.profession = profession

    def personInfo(self):
        return f"{super().personInfo()}, College: {self.college}, Profession: {self.profession}"

def Info(person):
    print(person.personInfo())

# 创建对象
person = Person("Alice", 30, "Female")
student = Student("Bob", 20, "Male", "Engineering", "CS101")
teacher = Teacher("Carol", 45, "Female", "Science", "Physics")

# 调用 personInfo 方法
person.personInfo()
student.personInfo()
teacher.personInfo()

# 调用 Info 函数
Info(person)
Info(student)
Info(teacher)
