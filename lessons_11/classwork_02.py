

import sqlite3

def select_user(name: str):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?;
            """,
            (name,)
        )
        session.commit()
        return cursor.fetchone()


def select_user(email: str):
   with sqlite3.connect("db.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE email = ?;
           """,
           (email,)
       )
       session.commit()
       return cursor.fetchone()

if __name__ == "__main__":
    print(select_products("Andrew"))