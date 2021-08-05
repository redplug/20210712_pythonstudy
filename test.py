# # 클래스를 선언
# class Student:
#     def __init__(self):
#         pass
# # 학생을 선언합니다.
# students = Student()

# print("isinstance(student, Student):", isinstance(students, Student))

class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass

# 학생을 선언합니다.
students = Student()

print("isinstance(student, Human):", isinstance(students, Human))
print("type(student == Human):", type(students) == Human)