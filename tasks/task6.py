"""
The program calculates the areas of three shapes (circle, triangle and rectangle).
The shape type is requested via user input,
after which we make a request for the characteristics of the figure:
if the user has selected a circle, we request its radius,
if a triangle, the lengths of its three sides,
if a rectangle, the lengths of its two sides.

"""
import math

square = 0
figure = input("Введите тип фигуры:\n").lower()

if figure == "круг":
    radius = int(input("Введите радиус круга:\n"))
    square = math.pi * radius ** 2
elif figure == "треугольник":
    side_a = int(input("Введите длину стороны А:\n"))
    side_b = int(input("Введите длину стороны B:\n"))
    side_c = int(input("Введите длину стороны C:\n"))
    p = (side_a + side_b + side_c) / 2.0               # semi_perimeter
    square = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
elif figure == "прямоугольник":
    side_a = int(input("Введите длину стороны А:\n"))
    side_b = int(input("Введите длину стороны B:\n"))
    square = side_a * side_b

print(f"Площадь {figure}а: {square:.2f}")
