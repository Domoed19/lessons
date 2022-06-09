class Animal:
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
