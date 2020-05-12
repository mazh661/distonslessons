from person import Person
from department import Department
d1 = Department("IT",1000,2000)
d2 = Department("ML",3000,4000)
print(d1.name)
print(d2.name)
p1 = Person("yerasyl",22,d1)
p2 = Person("kirito",20,d2)
print(p1.getAvgSalary())#1500
print(p2.getAvgSalary())#3500
print(p1.department.getData())
print(p1)