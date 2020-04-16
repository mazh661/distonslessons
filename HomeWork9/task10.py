#Статистика
S = int(input())
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
arr=[]
for i in range(S):
    n = int(input())
    arr.append(arr)
print(arr)
sel_sort(arr)
print(arr)
chet = []
chet_c =0
nechet = []
nechet_c = 0
for i in range(len(arr)):
    if arr[i]%2==0:
        chet.append(arr[i])
        chet_c = chet_c +1
    else:
        nechet.append(arr[i])
        nechet_c=nechet_c+1

if chet_c > nechet_c:
    print("YES")
else: 
    print("No")
    
