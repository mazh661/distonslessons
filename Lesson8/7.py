import json
student1={
    "name":"era",
    "mark":4.5,
    "marks":[5,5,5,3,4],
}
student2={
    "name":"china",
    "mark":5,
    "marks":[3,4,2,3,4],
}
students=[student1,student2]
with open("students.json","w") as filewrite:
    json.dump(students,filewrite,indent=4)
