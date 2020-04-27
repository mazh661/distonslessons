import random

n = int(input())
arr = []
for i in range(n):
    rnum = random.randint(0,20)
    arr.append(rnum)
def print_arr(array):
    print("Элементы массива:")
    for i in array:
        print(i)
    print("Максимальный элемент")
    get_max(array)
    print("Минимальный элемент")
    get_min(array)
    print("Средний элемент")
    get_avg(array)
def get_max(array):
    maxi=array[0]
    for i in array:
        if maxi<i:
            maxi = i
    print(maxi)
def get_min(array):
    mini=array[0]
    for i in array:
        if mini>i:
            mini = i
    print(mini)
def get_avg(array):
    sumi=0
    arf=0
    for i in array:
        sumi=sumi+i
    arf=sumi/i
    print(arf)

print_arr(arr)






