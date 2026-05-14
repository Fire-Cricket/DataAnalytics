# Jordan R. Worrobah
# 5/13/2026
# OOP Practice

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")
        print("-------------------")

student1 = Student("Alice", 95)
student2 = Student("Bob", 88)


print(f"Student 1: {student1.name}, Grade: {student1.grade}")
print(f"Student 2: {student2.name}, Grade: {student2.grade}")
print()

student1.display_info()
student2.display_info()