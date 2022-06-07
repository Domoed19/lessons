"""Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""
def cities_and_countrys (city):
    mapping = {
        "Belarus" : ["Minsk", "Grodno", "Gomel"],
        "UK" : ["London", "Manchester", "Bristol"],
        "USA": ["Los Angeles", "New York", "Chicago"],
        "Germany": ["Berlin", "Hamburg", "Cologne"],
    }
    for country, cities_list in mapping.items():
        if city in cities_list:
            return country
print(cities_and_countrys (input("Введите город: ")))
