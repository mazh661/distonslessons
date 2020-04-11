import random
n,m = input().split()
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    temp=[]
    sumi=0
    for j in range(m):
        rnum = random.randint(0,20)
        temp.append(rnum)
        sumi =sumi + temp[j]
    arr.append(sumi)
for i in range(n):
    print(arr[i])