a = []  # заводим пустой список
n = int(input())  # считываем количество элемент в списке
for i in range(n):  
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)