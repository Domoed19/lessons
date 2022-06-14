"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.

"""
from solution_01 import Circle, Triangle, Square

fig = ["Circle", "Triangle", "Square"]

if __name__ == "__main__":
    circleresult = Circle(6, 2, 8)
    circleresult.area()
    triangleresult = Triangle(6, 1, 2, 3, 7, 7)
    triangleresult.area()
    squareresult = Square(5, 3, 4, 9)
    squareresult.area()

squares = [circleresult.area(), triangleresult.area(), squareresult.area()]
d = dict(zip(fig, squares))
print(d)
