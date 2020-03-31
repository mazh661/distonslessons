a = [int(s) for s in input().split()]
x = a[0]
y = a[1]
z = a[2]

sumi=x+y-z
if sumi>=0:
    print(sumi)
else:
    print("Impossible")
