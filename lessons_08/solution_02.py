"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при
инициализации устанавливает марку Mercedes, модель E500, год выпуска 2000.
Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""
from solution_01 import car
class NewCar(car):
    def change_names(self, new_brand, new_model, new_year):
        self.brand = new_brand
        self.model = new_model
        self.model = new_year
    def speedup1(self):
        while self.speed < 100:
            self.speed += 5
            print(f"{self.speed} km/h.")
if __name__ == "__main__":
    car = NewCar("Mercedes", "E500", 2000, 0)
    car.speedup1()