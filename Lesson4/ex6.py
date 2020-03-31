arr = []
n = int(input())

for i in range(n):
    arr.append(int(input()))

f = int(input())
k = 0
for i in arr:
    if i == f:
        k=1

if k==1:
    print("Yes")
else:
    print("No")
        
