"""
Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей.
"""
import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()

if __name__ == "__main__":
    create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)
    create_user("Nick", "Sim", "kilzil16@gmail.com", "qweerty", 25)
    create_user("Ludka", "Kach", "ludka@gmail.com", "12345678", 24)
    create_user("Andrew", "Keizo", "keizo@gmail.com", "TestPass", 22)
    create_user("Vovan", "Guz", "vovan@gmail.com", "asdfg", 26)
