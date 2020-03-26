a , b , c = input("Write 3 salary with space:").split()
s1 = int(a) 
s2 = int(b)
s3 = int(c)

#max s1 min s3
c1 = s1 > s2 and s2 > s3 

#max s1 min s2
c2 = s1 > s3 and s3 > s2

#max s2 min s3
c3 = s2 > s1 and s1 > s3

#max s2 min s1
c4 = s2 > s3 and s3 > s1

#max s3 min s1
c5 = s3 > s2 and s2 > s1

#max s3 min s2
c6 = s3 > s1 and s1 > s2

if c1:
    print(s1 - s3)
elif c2:
    print(s1 - s2)
elif c3:
    print(s2 - s3)
elif c4:
    print(s2 - s1)
elif c5:
    print(s3 - s1)
elif c6:
    print(s3 - s2)



