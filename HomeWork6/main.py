
import random
n,m = input().split()
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    temp=[]
    for j in range(m):
        rnum = random.randint(0,20)
        temp.append(rnum)
    arr.append(temp)
for i in range(n):
    print(arr[i])
# n-строк
# m-столбцы
# 3 4 5 6
# 1 2 3 4
# 4
# 4
# 1 2 3 4
# 5 5 6 7
# 7 4 3 1
# 2 3 4 5
# arr[строку][колонна]
sumi_arr = []
for i in range(m):
    sumi=0
    for j in range(n):
        sumi = sumi+arr[j][i]  
    print(sumi)
    sumi_arr.append(sumi)
print(sumi_arr)

maxi = 0
x=0
for i in range(len(sumi_arr)):
    if sumi_arr[i]>maxi:
        maxi=sumi_arr[i]
        x=i
print("index of max: " + str(maxi) + " is " + str(x))
#создать массив sumi_arr
#если 4 столбца то 4 элемента
#индекс суммы 0 в массие значит это нулевой столбец
#найти максимальный эелмент в массиве sumi_arr и запомнить его индекс
#через индекс можно понять какой столбец

