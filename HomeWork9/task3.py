#Конечные автоматы
k = int(input())

for i in range(k):
    n,m=input().split()
    n = int(n)
    m = int(m)
    d = 19*m + (n+239)*(n+366)/2
    print(d)

