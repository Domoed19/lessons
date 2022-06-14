"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
методы: нахождение периметра и площади окружности), Triangle
(атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""
import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Figure:
    def area(self) -> int:
        self.area = area
    def perimetr(self) -> int:
        self.perimetr = perimetr

class Circle(Figure):
    def __init__(self, x: int, y: int, r: int):
        self.x = x
        self.y = y
        self.r = r
    def area(self) -> int:
        return math.pi * self.r**2

    def perimetr(self) -> int:
        return 2 * math.pi * self.r

class Triangle(Figure):

    def __init__(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def perimetr(self) -> int:
        sidea = math.sqrt(abs(self.x1 - self.x2) ** 2 + abs(self.y1 - self.y2) ** 2)
        sideb = math.sqrt(abs(self.x2 - self.x3) ** 2 + abs(self.y2 - self.y3) ** 2)
        sidec = math.sqrt(abs(self.x3 - self.x1) ** 2 + abs(self.y3 - self.y1) ** 2)
        return sidea + sideb + sidec


    def area(self) -> int:
        sidea = math.sqrt(abs(self.x1 - self.x2) ** 2 + abs(self.y1 - self.y2) ** 2)
        sideb = math.sqrt(abs(self.x2 - self.x3) ** 2 + abs(self.y2 - self.y3) ** 2)
        sidec = math.sqrt(abs(self.x3 - self.x1) ** 2 + abs(self.y3 - self.y1) ** 2)
        per = (sidea + sideb + sidec)/2
        return math.sqrt(per * (per - sidea) * (per - sideb) * (per - sidec))

class Square(Figure):

    def __init__(self, x: int, y: int, x2: int, y2: int):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
    def area(self) -> int:
        side = math.sqrt(abs(self.x - self.x2) ** 2 + abs(self.y - self.y2) ** 2)
        return side * side
    def perimetr(self)-> int:
        side = math.sqrt(abs(self.x - self.x2) ** 2 + abs(self.y - self.y2) ** 2)
        return 4 * side

if __name__ == "__main__":
    circleresult = Circle(2, 4, 5)
    circleresult.area()
    circleresult.perimetr()
    print("Area - ", circleresult.area(), "Perimetr - ", circleresult.perimetr())

    squareresult = Square(2, 4, 6, 9)
    squareresult.area()
    squareresult.perimetr()
    print("Area - ", squareresult.area(), "Perimetr - ", squareresult.perimetr())
    triangleresult = Triangle(2, 4, 2, 9, 3, 5)
    triangleresult.area()
    triangleresult.perimetr()
    print("Area - ", triangleresult.area(), "Perimetr - ", triangleresult.perimetr())





