data=[
    {
        "name":"Yerassyl",
        "age":22,
    },
    {
        "name":"Kirito",
        "age":19,
    },
    {
        "name":"Noragami",
        "age":25,
    }
]
n = len(data)
names=[data[i]['name'] for i in range(n) if data[i]['name']!="Kirito"]
ages =[i['age'] for i in data]
print(names)
print(ages)