def limit(start,end,step):
    for i in range(start,end,step):
        print(i)
def print_arr(array):
    print("Элементы массива:")
    for i in array:
        print(i)
    print("Максимальный элемент")
    getMax(array)


def getMax(array):
    maxi=array[0]
    for i in array:
        if maxi<i:
            maxi = i
    print(maxi)

#limit(100,200,2)
a = [1,2,3,123,123]
print_arr(a)