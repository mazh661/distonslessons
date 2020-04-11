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
sums=[]
for i in range(n):
    sumi=0
    for j in range(m):
        sumi = sumi +arr[i][j]
    sums.append(sumi)
for i in range(n):
    print(arr[i])
    maxi = 0
    if maxi == arr[i]:
        maxi=arr[i]


print(i)