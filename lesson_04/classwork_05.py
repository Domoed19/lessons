"""Получить сумму кубов натуральных чисел от n до m используя цикл for,
 числа n и m вводятся с клавиатуры."""

m = abs(int(input("Lets go M")))
n = abs(int(input("Lets go N")))
result = 0
for item in range(n, m+1):
    result += item ** 3
print(result)