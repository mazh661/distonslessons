class Person:
    def __init__(self,n,a,d):
        self.name = n
        self.age = a
        self.dog = d
    def __str__(self):
        s=f"Person {self.name} with age {self.age} has {self.dog}"
        return s
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
    def getDogName(self):
        return self.dog.name
    def getDogAge(self):
        return self.dog.age