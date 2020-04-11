import random
import math
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

l = len(arr)
x = 0
y = 0
kor_arr=[]
for i in range(l):
    for j in range(len(arr[i])):
        if arr[i][j]==1:
            y,x=i,j
    print(y,x)
    kor_arr.append([y,x])
print(kor_arr)

A = int(input("Chose a point of A: "))
B = int(input("Chose a point of B: "))

Y = kor_arr[A][0] - kor_arr[B][0]
X = kor_arr[A][1] - kor_arr[B][1]

ab = math.sqrt(math.pow(X,2)+math.pow(Y,2))
        
print("AB = " + str(ab))    

  
        

    

