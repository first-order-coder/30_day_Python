class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        # print(f'{name}\n{age}\n{grades}\n', end='')

    def get_grades(self):
        return self.grades
    
class Course(Student):

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += self.get_grades()
        
        return value / len(self.students) 

s1 = Student('Tim', 22, 95)
s2 = Student('Gin', 32, 85)
s3 = Student('hen', 23, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
# print(course.students[0].name)
print(course.get_average_grade())

# c1 = Course()
# print(c1.add_student())
