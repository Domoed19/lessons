from sqlalchemy.orm import sessionmaker, Session

from models import Base, User, Profile, Address, Product_list
from utils import setup_db_engine, create_database_if_not_exists

# def create_user(
#         session: Session, email: str, password: str, phone: str, age: int, city:str, address: str
# ) -> User:
#
#     user = User(email=email, password=password)
#     profile = Profile(user=user, phone=phone, age=age)
#     address = Address(user=user, city=city, address=address)
#
#     session.add_all([user, profile, address])
#     session.commit()
#
#     return user
# def update_or_create(session: Session, user: User, city: str, address: str) -> Address:
#     if len(user.addresses):
#         current_address = user.addresses[0]
#         current_address.city = city
#         current_address.address = address
#     else:
#         address = Address(user=user, city=city, address=address)
#
#     session.add_all([user, address])
#     session.commit()
#
#     return address


# def create_product_list(
#         session: Session, name: str, price: int, amount: int, comment: str
# ) -> Product_list:
#     product_list = Product_list(name=name, price=price, amount=amount, comment=comment)
#
#     session.add(product_list)
#     session.commit()

def update(session: Session, name: str, price: int, amount: int, comment: str) -> Product_list:
    current_id = product_list.amount
    session.add(product_list)
    session.commit()



if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    # new_user = create_user(
    #     session=current_session,
    #     email="sadas@gmail.com",
    #     password="12312313",
    #     phone="3753382821283",
    #     age=19,
    #     city="Minsk",
    #     address="Timyriazeva"
    # )
    # new_user2 = create_user(
    #     session=current_session,
    #     email="cdc@gmail.com",
    #     password="434242342",
    #     phone="3752984477",
    #     age=29,
    #     city="Minsk",
    #     address="Timyriazeva"
    # )
    #user = current_session.query(User).filter_by(email="test@test.com").first()
    # address = Address(user=user, city="New city", address="New address")
    # current_session.add(address)
    # current_session.commit()

    #update_or_create(session=current_session, user=user, city="New City", address="New Address")

    # product_list1 = create_product_list(
    #     session=current_session,
    #     name="Xbox",
    #     price=1500,
    #     amount=1,
    #     comment="Есть на складе"
    # )
    #
    # product_list2 = create_product_list(
    #     session=current_session,
    #     name="Iphone11",
    #     price=1600,
    #     amount=12,
    #     comment="Есть на складе"
    # )
    #
    # product_list3 = create_product_list(
    #     session=current_session,
    #     name="Samsung TV",
    #     price=2100,
    #     amount=18,
    #     comment="Есть на складе"
    # )
    #
    # product_list4 = create_product_list(
    #     session=current_session,
    #     name="Microwave LG",
    #     price=700,
    #     amount=1,
    #     comment="Товар отсутствует"
    # )





