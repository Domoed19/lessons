"""Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина.
Каждая строка входного файла представляет собой запись вида
Покупатель, Товар, Количество, Стоимость где
Покупатель - имя покупателя (строка без пробелов), товар - название товара (строка без пробелов),
количество - количество приобретенных единиц товара.
Создайте список и выведите на экран всех покупателей, а для каждого
покупателя подсчитайте общее количество приобретенных им товаров и их стоимость.
Создайте список и выведите на экран все товары, а для каждого
товара подсчитайте общее количество приобретенных и их стоимость."""

import csv




def tovari_spis (text: str) -> dict:
    text = text.replace(",", " ").split()
    for word in text:
        word = word.strip()
    return word

with open("tovari.csv", "r") as file:
   reader = csv.reader(file)
   for row in reader:
       for col in row:
           print(tovari_spis(col))





