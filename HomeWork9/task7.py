#Разварот
s = int(input())
arr = [int(s) for s in input().split()]

print(arr)

new_arr = []
while s > 0:

    new_arr.append(arr[s-1])
    s-=1

print(new_arr)
