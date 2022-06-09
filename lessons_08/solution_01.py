"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задний ход (изменение знака скорости)."""

class car:
    brand: str = None
    model: str = None
    year: int = None
    speed: int = None

    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    def speedup(self):
        self.speed = self.speed + 5
        print("Скорость: ", self.speed)
    def speeddown(self):
        self.speed = self.speed - 5
        print("Скорость: ", self.speed)
    def stop(self):
        self.speed = 0
        print("Стоп: ",self.speed)
    def speedinfo(self):
        self.speed = self.speed
        print("Speedinfo: ",self.speed)
    def reverse(self):
        if self.speed < 0:
            print("Revers")
if __name__ == "__main__":
    car = car("BMW", "330i", 2009, 0)
    car.speedup()
    car.speeddown()
    car.stop()
    car.speedinfo()
    car.reverse()