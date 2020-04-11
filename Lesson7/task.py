import random
n,m = input().split()
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(0)
    arr.append(temp)

for i in range(n):
    index=random.randint(0,m-1)
    arr[i][index]=1
for i in range(n):
    print(arr[i])