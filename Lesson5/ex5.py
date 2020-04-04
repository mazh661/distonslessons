arr=["asdad",1,"asdasd",1,"asdadsa",300,"asdasda",2000,"!!",300,"asdsad",300,"asdasd"]
startnum=0
startword=0
n = len(arr)
try:
    num = int(arr[0])
    startnum = 0
    startword = 1
except:
    startnum = 1
    startword = 0
numbers=arr[startnum:n:2]
words=arr[startword:n:2]
print(numbers)
print(words)