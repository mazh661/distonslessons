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
    maxi=0
    marks=i['marks']
    n = len(marks)
    for j in range(n):
        if maxi<marks[j]:
            maxi = marks[j]
    i['mark']=maxi
    print(maxi)

for i in students:
    print(i)
