#create array
arr = [3,4,4]#[]
print("Before",arr)
arr.append(42)
arr.append(50)
arr.append(20)
print("After",arr)
#the length of array
n = len(arr)
print("Length",n)
#index
#3 4 4 42 50 20
#0 1 2 3   4  5
#first element
first = arr[0]
print("First element",first)
#last element
last = arr[n-1]
print("Last element",last)
#delete element
arr.pop(3)
print("After deleting",arr)
#delete element
arr.remove(4)
print("After deleting",arr)
#getIndex of element
index = arr.index(50)
print("Index of 50",index)
#replace of elements
arr[2]=14444
print("Replace",arr)