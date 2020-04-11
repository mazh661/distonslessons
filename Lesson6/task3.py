arr = [
    [1, 2,  3, 4,  5],
    [6, 7,  8, 9,  10],
    [11,12, 13,14, 15],
    [16,17, 18,19, 20],
    [21,22, 23,24, 25]

]

n = len(arr)
f = int(input())
k=0
for i in range(n):
    m = len(arr[i])
    for j in range(m):
        if arr[i][j] == f:
            if i+j+1<n:
                k=1
            elif i+j+1>n:
                k=2
            elif i+j+1==n:
                k=3
            else:
                k=0

if k == 0:
    print("Errror")
elif k == 1:
    print("Top")
elif k == 3:
    print("Middle")
elif k == 2:
    print("Down")