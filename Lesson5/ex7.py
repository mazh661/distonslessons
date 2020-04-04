arr=[
    [0,1,1],
    [1,0,0]
]
# arr=[1,2,3]
count=0
#take array
for i in range(len(arr)):
    temparr = arr[i]
    #go into array
    for j in temparr:
        if j == 1:
            count=count+1
print(count)