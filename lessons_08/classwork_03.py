""
from classwork_01 import Dog

class cat(Dog):
    def meow(self):
        print(f"{self.name} is meowing.")
if __name__ == "__main__":
    dog = Dog(10, 5, "Test", 10)
    dog.jump()
    dog.run()
    dog.bark()

    cat = Cat(12, 6, "Tt", 15)
    cat.run()