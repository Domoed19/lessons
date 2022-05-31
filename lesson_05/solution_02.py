"""Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить,
причем сам себе человек не может подарить, дубликаты тоже не допустимы.
"""


def secret(tot_kto_darit, tot_komu_daryat):
    for person1 in tot_kto_darit:
        for person2 in tot_komu_daryat:
            if not person1 in listik and not person2 in listik2 and not person2 in tot_kto_darit:
                result.append(person1 + "--" + person2)
                listik.append(person1)
                listik2.append(person2)
    return result

result = []
listik = []
listik2 = []

list1 = ["маша", "коля", "люда"]
list2 = ["витя", "олег", "ира"]

print(secret(list1, list2))


