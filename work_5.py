# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


x1 = float(input('Введите первое значение точки A:'))
x2 = float(input('Введите первое значение точки B:'))
print('A','(', x1, ';' , x2, ')' )
y1 = float(input('Введите второе значение точки A:'))
y2 = float(input('Введите второе значение точки В:'))
print('B','(', y1, ';' , y2, ')' )
Num = (((x2 - x1)**2) + ((y2 - y1)**2))
sqrt = math.sqrt(Num)
print(sqrt)

