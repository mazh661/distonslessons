class Person:
    def __init__(self, name,age,department):
        self.name = name
        self.age = age
        self.department = department
    def setName(self,name):
        self.name = name
    
    def getMyDepartmentName(self):
        return self.department.name

    def getAvgSalary(self):
        avg_salary = (self.department.max_salary+self.department.min_salary)/2
        return avg_salary


    def getName(self):
        return self.name
    
    def setAge(self,age):
        self.age = age

    def getAge(self):
        return self.age
        
    def __str__(self):
        s = f"Name:{self.name},Age:{self.age},Department:[{self.department}]"
        return s
