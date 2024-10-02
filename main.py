import math

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = float(input("Введите z от -1 до 1: "))
b = math.sqrt(10 * (x * (1. / 3.) + x * (y + 2))) * ((math.asin(z) ** 2) - abs(x - y))
print('Ответ: ')
print(b)
