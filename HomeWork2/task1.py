#Basketball
i=0
sum1 = 0
sum2 = 0
for i in  range(4):
    a, b = input().split()
    c = int(a)
    d = int(b)
    sum1 = sum1 + c
    sum2 = sum2 + d

if sum1 > sum2:
    print("1")
elif sum1 < sum2:
    print("2")
else:
    print("Draw")



