arr=["Hello","1231321","!!@#@!","1231"]
numbers=[]
words=[]
n = len(arr)
for i in range(n):   
    try:
        n = int(arr[i])
        numbers.append(arr[i])
    except:
        words.append(arr[i])

print("Numbers ", numbers)
print("Words", words)