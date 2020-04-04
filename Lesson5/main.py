n = int(input())
arr=[int(i) for i in input().split()]
sumi=0
for i in range(n):
    sumi = sumi + arr[i]
print(sumi)