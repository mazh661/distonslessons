arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
num = int(input())
x = 0
y = 0
k = 0
for i in range(len(arr)):
    temparr = arr[i]
    for j in range(len(temparr)):
        if temparr[j]==num:
            x = i
            y = j
            k = 1
if k==1:
    print(x,y)
elif k==0:
    print("Not found")