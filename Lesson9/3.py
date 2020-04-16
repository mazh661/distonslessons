#5
#1 2 1 2 3 
#1)они должны генерироваться рандомно используя генератор 
#2)нужно вывести ск ко раз встречается каждый элемент
#3)if i in ...
#4)сортировка
# 1 - 2
# 2 - 2
# 3 - 1

import random
print(arr)
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


n = int(input())                                                              
arr=[random.randint(0,20) for i in range(n)]

sel_sort(arr)
print(count)
        