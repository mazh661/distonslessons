peoples=[
    {
        "name":"Yerassyl",
        "age":22,
        "balance":10000,
        "department_id":1,
    },
    {
        "name":"kirito",
        "age":21,
        "balance":1000,
        "department_id":1
    },
    {
        "name":"zoka",
        "age":19,
        "balance":5000,
        "department_id":2
    }
]
def checkDepartmentId(data,department_id):
    for i in data:
        if i['department_id']==department_id:
            return None
    return "No user with that department"
def getPeopleByDepartmentId(data,department_id):
    searched_data=[]
    err = checkDepartmentId(data,department_id)
    if err!=None:
        return [],err
    for i in data:
        if i['department_id']==department_id:
            searched_data.append(i)
    return searched_data,None
newpeople,err = getPeopleByDepartmentId(data=peoples,department_id=0)
if err!=None:
    print(err)
else:
    print(newpeople)