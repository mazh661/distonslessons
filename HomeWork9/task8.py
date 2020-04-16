#Оттепель
s = int(input())
arr = [int(s) for s in input().split()]
count = 0
maxi = 0
for i in range(len(arr)):
    if arr[i]>0:
        count+=1
        if maxi<count:
            maxi=count
    else:
        count=0

print(maxi)
