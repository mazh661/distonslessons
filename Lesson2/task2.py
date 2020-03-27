a = int(input())
b = int(input())
c = int(input())
ndm = 0

if a>b and a<c:
    ndm = a 
elif b>a and b<c:
    ndm = b
elif c>a and c<b:
    ndm = c

print(ndm)