arr=[-2,45,0,11,-9]
mini=0
maxi=0
for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    if arr[j]<mini:
        mini=arr[j]

    if arr[i]>maxi:
            maxi=arr[i]
    

print(arr)
print(mini)
print(maxi)