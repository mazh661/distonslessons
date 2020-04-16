def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print("Площадь: %.2f" % (a*b))
 
def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %.2f" % (0.5 * a * h))
 
def circle():
    r = float(input("Радиус: "))
    print("Площадь: %.2f" % (3.14 * r**2))
 
figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
if figure == '1':
	rectangle()
elif figure == '2':
	triangle()
elif figure == '3':
	circle()
else:
	print("Ошибка ввода")