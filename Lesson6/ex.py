import random
n,m = input().split()
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    temp=[]
    for j in range(m):
        rnum = random.randint(0,20)
        temp.append(rnum)
    arr.append(temp)
for i in range(n):
    print(arr[i])