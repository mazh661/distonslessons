#От перестановки что-то меняется ...
a,b,c=input().split()
a = int(a)
b = int(b)
c = int(c)
print(a,b,c)

if a + b == c:
    print("YES")
elif a + c == b:
    print("YES")
elif b + c == a:
    print("YES")
else:
    print("NO")