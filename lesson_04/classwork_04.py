"""
Написать программу, которая будет выводить на экран случайные
числа от 1 до 10 до тех пор, пока не выпадет 7.
while True:
    x = random.randint(1, 10)
    if x = = 7:
        break
     print(x)
"""

"""import random

x = random.randint(1, 10)

    x = random.randint(1, 10)
    while x != 7:
        break
     print(x)"""
import random
while True:
    x = random.randint(1, 10)
    if x == 7:
        break
print(x)