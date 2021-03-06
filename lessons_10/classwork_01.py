"""
Создать функцию при помощи регулярных выражений для проверки,
что строка является валидным телефонным номером в формате
+375 (29) 299-29-29.
"""
import re
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

def is_mobile_phone(string):
    return re.match(r"^\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$", string)

if is_mobile_phone("+375 (29) 299-29-29"):
    print("Yes")
else:
    print("No")
#test for this programm
if __name__ == "__main__":
    for item in ("+375 (29) 299-29-29", "+375 (29) 299-29-29"):
        assert is_mobile_phone(item) is not None
#Здесь проверяем неправильные, если неправильно то не выводит
    for item in ("+(29) 299-29-29", "+375(29)299-29-29"):
        assert is_mobile_phone(item) is None

        logger.debug("All test are OK")




