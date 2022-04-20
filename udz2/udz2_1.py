from random import randint

names = ["Alex", "Mike", "Dave", "Fergus", "John"]


class Student:
    def __init__(self, name="Radomir", groupNumber=1213, age=18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, group_number):
        self.groupNumber = group_number


students = []
for name in names:
    students.append(Student(name, randint(1, 2000), randint(17, 30)))

for student in students:
    print(f"{student.name} | {student.age} | K{student.groupNumber} ")
