arr = []
sumi=0
n = int(input())

for i in range(n):
    arr.append(int(input()))
    sumi=sumi+arr[i]

print(sumi)