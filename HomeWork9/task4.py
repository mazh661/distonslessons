#Перепись
k = int(input())
arr = []
maxi=0
count=0
for i in range(k):
    n,m=input().split()
    n = int(n)
    m = int(m)
    arr.append([n,m])
    if m == 1:
        if n>maxi:
            maxi=n
            count=i+1
print(maxi, count)

