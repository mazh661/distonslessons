import json
students=[]
with open("students.json","r") as file:
    data = file.read()
    students = json.loads(data)
for i in students:
    print(i['name'])