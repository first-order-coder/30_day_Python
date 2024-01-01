class Employee:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

# class Salary:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender

#     def jump(self):
#         print(self.name,self.gender)

# class Male(Salary,Employee):
#     def __init__(self,name,gender,occupation):
#         self.occupation=occupation
#         super().__init__(name,gender)


employee1 = Male("Jim","male","technician")
employee2 = Employee('gin', 'Male')
# employee1.jump()
print(employee2)