"""Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе,
функция имеет два параметра: ссылка на файл и имя на файловой системе.
В качестве примера ссылки на файл можно использовать лицензию из ГитХаба и
з вашего репозитория: https://raw.githubusercontent.com/Domoed19/lessons/main/LICENSE"""

import requests
req = "https://raw.githubusercontent.com/Domoed19/lessons/main/LICENSE"
r = requests.get(req)
open("LICENSE", "wb").write(r.content)