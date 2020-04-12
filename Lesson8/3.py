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
students=[]
students.append(student1)
students.append(student2)
for i in students:
    marks=i['marks']
    n = len(marks)
    sumi=0
    for j in range(n):
        sumi = sumi + marks[j]
    print(i['name'],sumi/n)