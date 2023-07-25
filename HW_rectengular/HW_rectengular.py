# Домашнее задание:
#
# 1. Создайте класс `Shape` (Фигура), у
# которого есть метод `area()` (площадь) и метод `perimeter()` (периметр).
# Оставьте эти методы без реализации.
# - Создайте два подкласса класса `Shape`:
#
# -`Rectangle` (Прямоугольник), который принимает два аргумента `length` (длина) и
# `width` (ширина) при создании экземпляра класса. Реализуйте методы `area()` и
# `perimeter()` для расчета площади и периметра прямоугольника.
#
# -`Circle` (Круг), который принимает один аргумент `radius` (радиус) при создании
# экземпляра класса. Реализуйте методы `area()` и `perimeter()` для расчета
# площади и длины окружности круга.
#
# - Создайте объекты `Rectangle` и `Circle`,
# передавая необходимые значения при их создании.
#
# - Выведите на экран площадь и периметр
# прямоугольника и круга, используя соответствующие методы.

import math
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return (self.width + self.length) * 2
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


process = True
while process:
    admin = input('choose shape:  ')
    if admin.lower() == 'rect':
        a = int(input('length:   '))
        b = int(input('width:   '))
        rec = rectangle(a, b)
        print(f'rectangle area =', rec.area)
        print(f'rectangle perimeter =', rec.perimeter())
    elif admin.lower() == 'cir':
        r = int(input('radius:   '))
        cir = circle(r)
        print(f'circle area =', cir.area)
        print(f'circle perimeter =', cir.perimeter())
    elif admin.lower() == 'stop':
        process = False
        break
