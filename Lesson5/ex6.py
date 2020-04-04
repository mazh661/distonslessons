arr=[42,123,3894,212,422]
#slice
arr1=arr[0:3]
arr2=arr[3:5]
print(arr)
#вывести все элементы не включая последний
print("вывести все элементы не включая последний")
print(arr[0:4])
#вывксти все элементы кроме первого
print("вывести все элементы кроме первого")
print(arr[1:5])
print(arr[1:])
#массив[начало:конец:шаг]
print("with step 2")
print(arr[1:5:2])
#write each second element
print("write each second element")
print(arr)
print(arr[0:5:2])
n=len(arr)
print(arr[0:n:2])
print(arr[::2])
print(arr[::])