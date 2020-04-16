S = int(input())
arr = []
n = int(input())


def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
for i in range(n):
    m = int(input())
    arr.append(m)
print(arr)
sel_sort(arr)
print(arr)
count =0
s = 0
for i in range(len(arr)):
    if s < S:
        s=s+arr[i]
        count=count+1
print(count)
