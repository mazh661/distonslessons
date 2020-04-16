#счастливый билет
num = input()
arr = []
for i in num:
    a = int(i)
    arr.append(a)

print(arr)

f = arr[0]+arr[1]+arr[2]
s = arr[3]+arr[4]+arr[5]

    
if f==s:
    print("YES")
else:
    print("NO")