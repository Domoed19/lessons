"""Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
 Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя. """
"""
from classwork_01 import Dog
class NewDog(Dog):

    def __init__(self, height: int, weight: int, name: str, age: int):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.age += kwargs.get("name")
    
    def change_name(self, new_name):
    self.name = new_name
    что бы это применять надо поменять переменные в основной програме на self.height = kwargs.get("height")
    dog = Dog(height = 10, weight = 5, ...)
"""
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
    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    dog = Dog(10, 5, "Test", 10)
    dog.jump()
    dog.run()
    dog.bark()

    dog2 = Dog(12, 6, "Tt", 15)
    print("old name:", dog2.name)
    dog2.change_name("Chuk")
    print("New Name:", dog2.name)