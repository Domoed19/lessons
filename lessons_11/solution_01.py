"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""

import sqlite3

#def create_product(name: str, cost: int, ammount: int, commentary: str):
    #with sqlite3.connect("my_products.sqlite3") as session:
        #cursor = session.cursor()
        #cursor.execute(
            #"""
            #INSERT INTO products (name, cost, ammount, commentary)
            #VALUES (?, ?, ?, ?);
            #""",
            #(name, cost, ammount, commentary),
        #)
        #session.commit()


#if __name__ == "__main__":
    #create_product("Xbox", 1500, 1, "Есть на складе")
    #create_product("Iphone 11", 1600, 12, "Есть в наличии")
    #create_product("Tv Samsung", 2100, 15, "Есть на складе")
    #create_product("Microwave LG", 700, 0, "Товар отсутствует")


def select_products(from_id: int, to_id: int):
   with sqlite3.connect("my_products.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM products
           WHERE id >= ? and id <= ?;
           """,
           (from_id, to_id)
       )
       session.commit()
       return cursor.fetchall()

def udate_products(id:int):
   with sqlite3.connect("my_products.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           UPDATE products
           SET ammount = 12
           WHERE id = ?;
           """,
           (id,)
       )
       session.commit()
       return cursor.fetchone()

def delete_products(id:int):
   with sqlite3.connect("my_products.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           DELETE from products
           WHERE id = ?;
           """,
           (id,)
       )
       session.commit()
       return cursor.fetchone()

if __name__ == "__main__":
    print(select_products(1, 4))
    print(udate_products(3))
    print(delete_products(4))




