arr = []
nechet = []
chet = []
n = int(input())

for i in range(n):
    arr.append(int(input()))
    if arr[i]%2==0:
        chet.append(arr[i])
    else:
        nechet.append(arr[i])

print("Vse chisla ",arr)
print("Chetnye ", chet)
print("Nechetnye", nechet)
