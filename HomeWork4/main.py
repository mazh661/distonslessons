import math
arr=[] 
n = int(input("Количество чисел "))
for i in range(n):
    arr.append(int(input()))
founder = int(input("Найти наиближайщее число к "))
diff=[]
#math
for i in range(len(arr)):
    diff.append(math.fabs(founder-arr[i]))
mini=diff[0]
minindex=0
for i in range(len(diff)):
    if diff[i]<mini:
        mini=diff[i]
        minindex=i
print("Найближайщее число к ",founder, "- " ,arr[minindex])