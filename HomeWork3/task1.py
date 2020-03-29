x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

sumi=x+y-z
if sumi>=0:
    print(sumi)
else:
    print("Impossible")
