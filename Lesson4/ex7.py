arr = []
n = int(input())

for i in range(n):
    arr.append(int(input()))

f = int(input(""))
maxi = 0
l = len(arr)
for i in range(l):
    if i <= f and i >= maxi:
        maxi=i

print(arr[maxi])
     



        
