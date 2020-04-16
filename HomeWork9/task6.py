#Нули
num = input()
arr = []
for i in num:
    a = int(i)
    arr.append(a)

count = 0
maxi = 0
for i in range(len(arr)):
    if arr[i]==0:
        count+=1
        if maxi<count:
            maxi=count
    else:
        count=0

print(maxi)