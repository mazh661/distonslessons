class Department:
    def __init__(self,name,min_salary,max_salary):
        self.name = name
        self.min_salary = min_salary
        self.max_salary = max_salary
    def getData(self):
        s=f"DepartmentName:{self.name},MinSalary:{self.min_salary},MaxSalary:{self.max_salary}"
        return s
    def __str__(self):
        s=f"DepartmentName:{self.name},MinSalary:{self.min_salary},MaxSalary:{self.max_salary}"
        return s