"""Ввести с клавиатуры строку, проверить является ли строка палиндромом
и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые о
динаково читаются слева направо и справа налево"""

n = input("Введите слово")
m = "".join(n)
print(m)
if m == m[::-1]:
    print("yes")
else:
    print("no")
