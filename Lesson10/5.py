import random 
arr=[random.randint(0,20) for i in range(5)]
print(arr)
def getMax(array):
    maxi=array[0]
    for i in array:
        if maxi<i:
            maxi = i
    return maxi

def using_max(max_element):
    print("Max Element",max_element)

return_max = getMax(arr)
using_max(return_max)