arr=[
    [1,2,3,4],
    [5,6,7,8],
    [9,8,7,6],
    [5,4,3,2]
]
n = len(arr)
sumi=0
for i in range(n):
    m = len(arr[i])
    for j in range(m):
        if i+j+1<n:
            sumi=sumi+arr[i][j]
print(sumi)