"""В школе решили набрать три новых класса по программированию. Так как занятия у них проходят в одно и то же время,
было решено выделить кабинет для каждого класса и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их
хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
"""
x = int(input("Chislo uchenikov"))
y = int(input("Chislo uchenikov"))
z = int(input("Chislo uchenikov"))

if x % 2 == 0:
    x == x
else:
    x += 1
if y % 2 == 0:
    y == y
else:
    y += 1
if z % 2 == 0:
    z == z
else:
    z+=1

f = lambda x, y, z: (x + y + z)/2
result = f(x, y, z)

print(result)