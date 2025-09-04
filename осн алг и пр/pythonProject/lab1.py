import math
print("Введите переменные a,b и с")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = b**2-4*a*c
if d == 0:
    x1 = -b/(2*a)
    print("Один корень: ", x1)
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Два корня:")
    print("x1 = ", x1)
    print("x2 = ", x2)
if d < 0:
    print("Нет корней")