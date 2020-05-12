class Dog:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
    def __str__(self):
        s=f"Dog with {self.name} and age {self.age}"
        return s