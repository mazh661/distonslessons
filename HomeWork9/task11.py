n = int(input())
big_arr=[]
for i in range(n):
    arr = [int(s) for s in input().split()]
    big_arr.append(arr)
counter=0
for i in big_arr:
    for j in i:
        if j ==1:
            counter+=1
print(counter//2)
