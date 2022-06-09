"""Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты."""

"""
Для параметра age по умолчанию
class Dog:
    height = None
    weight = None
    name = None
    age = 10

    def __init__(self, height, weight, name, age: int = None):
        self.height = height
        self.weight = weight
        self.name = name
        if age is not None:
        self.age = age
dog = Dog(10, 5, "Test")"""



class Dog:
    height: int = None
    weight: int = None
    name: str = None
    age: int = None

    def __init__(self, height: int, weight: int, name: str, age: int):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
    def jump(self):
        print(f"{self.name} is jumping.")
    def run(self):
        print(f"{self.name} is running.")
    def bark(self):
        print(f"{self.name} is barking.")

if __name__ == "__main__":
    dog = Dog(10, 5, "Test", 10)
    dog.jump()
    dog.run()
    dog.bark()

    dog2 = Dog(12, 6, "Tt", 15)
    dog2.run()
