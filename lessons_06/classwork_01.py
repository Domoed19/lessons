"""Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский,
где слово - это входной параметр, вторая функция - с русского на английский."""

slovar = {"apple":"яблоко", "sun":"солнце", "screwdriver":"отвертка"}

def pervod_s_angl_na_rus (slovo):
    return slovar[slovo]


def pervod_s_rus_na_angl(slovo):
    for key, value in slovar.items():
        if value == slovo:
            return key

def perevert (slovo):
    new_dict = {
        value:key
        for key, value in slovar.items()
    }
    return new_dict[slovo]

print (pervod_s_angl_na_rus("sun"))
print (pervod_s_rus_na_angl("солнце"))
print (perevert("солнце"))
