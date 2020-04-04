arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sumi2=0
sumi1=0
for i in range(len(arr)):
    temparr = arr[i]
    #go into array
    for j in temparr:
        if j%2 == 0:
            sumi2=sumi2+j
        else:
            sumi1=sumi1+j
print("Summa chet",sumi2)
print("Summa nechet", sumi1)