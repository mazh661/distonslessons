#Две окружности
x,y,r = input().split()
x1,y1,r1 = input().split()
x = int(x)
y = int(y)
r = int(r)
x1 = int(x1)
y1 = int(y1)
r1 = int(r1)

R = r + r1
X = x - x1
Y = y - y1

if R**2 >= (X**2)*(Y**2):
    print("YES")
else:
    print("No")