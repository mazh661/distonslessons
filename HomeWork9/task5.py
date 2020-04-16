#Кругляши
num = input()
arr = []
count=0
for i in num:
    a = int(i)
    if a == 0 or a == 6 or a == 9:
        count+=1
    elif a == 8:
        count+=2

print(count)