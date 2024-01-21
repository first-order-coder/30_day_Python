from datetime import datetime

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f'Name: {self.name} and Age is: {self.age}')

class Student(Person): #cereating a child class of Person(inheritance)
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #the assigned attribute in parent class wont change and we are able to use them without rearranging
        self.student_id = student_id
        self.enrollments = []

    def enroll(self, enrollment):
        if enrollment not in self.enrollments:
            self.enrollments.append(enrollment)
            enrollment.add_student(self)
            print(f"{self.name} is")

class Professor(Person):
    def __init__(self,name, age, employee_id):
        super().__init__(name, age) #super().__init__ is used most when inheritance is used in code
        self.employee_id = employee_id
        self.courses_taught = []

    def teach(self, course):
        pass

class Course:
    def __init__(self, course_title, code, max_students):
        self.course_title = course_title
        self.code = code
        self.max_students = max_students
        self.students = []
        self.professor = []
    
    def set_professor(self, professor):
        pass

    def add_student(self, student):
        if len(self.students) < self.max_students:
            enrollment = Enrollment(student)


class Enrollment:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
        self.assignments = []
    
    def set_course(self):
        pass
    
    def add_assignement(self):
        pass

    def submit_assignment(self):
        pass

class Assignment:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def set_grade(self):
        pass
