import random
import math
n,m = input().split()
n = int(n)
m = int(m)
s = int(input())
arr=[]
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(0)
    arr.append(temp)

for i in range(n):
#     index1=random.randint(0,m-1)
#     # inde2=random.randint(0,m-1)
#     index3=random.randint(0,m-1)
#     index4=random.randint(0,m-1)
#     index5=random.randint(0,m-1)
#     arr[i][index1]=1
#     arr[i][index2]=1
#     arr[i][index3]=1
#     arr[i][index4]=1
#     arr[i][index5]=1
    
    for j in range(s):
        index=random.randint(0,m-1-j)
        arr[i][index]=1
        
for i in arr:
    print(i)
import json
with open("game.json","w") as file:
    json.dump(arr,file,indent=2)