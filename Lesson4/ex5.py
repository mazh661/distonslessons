arr = []
arf = 0
sumi = 0
n = int(input())

for i in range(n):
    arr.append(int(input()))
    sumi=sumi+arr[i]
arf=sumi/n
print("ARF ", arf)
