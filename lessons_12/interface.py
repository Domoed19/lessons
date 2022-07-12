"""
Создать программу с пользовательским интерфейсом позволяющим
выбирать определенную функцию и вводить необходимые данные.
"""

from main import create_product_list, get_product_list, update_prod, del_prod, buying, all_buying, \
    purchase_filtration, current_session
TEMPLATE = """
 Выберите один из вариантов:
    1. Создать список продуктов
    2. Напечатать все продукты
    3. Обновить продукт по ID
    4. Удалить продукт по ID
    5. Купить продукт
    6. Напечатать все покупки
    7. Отфильтровать покупки
"""
def main():
    while True:
        try:
            user_choice = int(input(TEMPLATE))
        except ValueError:
            user_choice = None

        if user_choice == 1:
            print("Введите name, price через запятую:")
            name, price, ammount, comment = input().split(',')
            create_product_list(current_session, name, int(price), int(ammount), comment)
        elif user_choice == 2:
            for products in get_product_list(current_session):
                print(products)
            else:
                return print("Нет продуктов")
        elif user_choice == 3:
            print("Введите name, price через запятую:")
            name, price = input().split(',')
            update_prod(current_session, name, int(price))
        elif user_choice == 4:
            print("Введите id продукта для удаления")
            id = int(input())
            del_prod(current_session, id)
        elif user_choice == 5:
            print("Введите product_id, user_id, ammount через запятую:")
            product_id, user_id, ammount = input().split(',')
            buying(current_session, int(product_id), int(user_id), int(ammount))
        elif user_choice == 6:
            for purchases in all_buying(current_session):
                print(purchases)
            else:
                return print("Нет покупок")
        elif user_choice == 7:
            purchase_filtration(current_session)
            print("Фильтрация")
        else:
            print("None")

if __name__ == "__main__":
    main()












