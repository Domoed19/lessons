"""Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле."""


def format_string (name):
    print(f"Hello, {name}")


my_names = ["Kirill", "Vitya", "Petya", "Kolya", "Inna"]
for name in my_names:
    format_string(name)