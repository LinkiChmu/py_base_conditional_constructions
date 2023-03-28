import math
"""Программа вычисляет площади трех фигур (круг, треугольник и прямоугольник).
Тип фигуры запрашиваем через пользовательский ввод,
после чего делаем запрос характеристик фигуры:
если пользователь выбрал круг, запрашиваем его радиус,
если треугольник – длины трех его сторон;
если прямоугольник – длины двух его сторон.
"""
square = 0
figure = input("Введите тип фигуры:\n").lower()
if figure == 'круг':
    radius = int(input("Введите радиус круга:\n"))
    square = round(math.pi * radius**2, 2)
    print("Площадь круга:", square)
elif figure == 'треугольник':
    side_a = int(input("Введите длину стороны А:\n"))
    side_b = int(input("Введите длину стороны B:\n"))
    side_c = int(input("Введите длину стороны C:\n"))
    p = (side_a + side_b + side_c) / 2.0  # calculate semi_perimeter
    square = round(math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c)), 2)
    print("Площадь треугольника:", square)
elif figure == 'прямоугольник':
    side_a = int(input("Введите длину стороны А:\n"))
    side_b = int(input("Введите длину стороны B:\n"))
    square = side_a * side_b
    print("Площадь прямоугольника:", square)

