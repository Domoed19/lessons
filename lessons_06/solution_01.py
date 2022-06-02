"""Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное, в идеале не использовать библиотечные функции.
"""
import collections

text = input("Введите текст:")
text = text.split()

def max_vs(element):

    cv = collections.Counter(element)
    most_ch = cv.most_common()[0]
    return most_ch

def max_elem(element):
    longest_word =  max(element, key=len)
    return longest_word
print (max_elem(text))
print (max_vs(text))



