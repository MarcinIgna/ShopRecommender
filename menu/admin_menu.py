from models.base_model import BaseModel
from models.user import Users
from models.product import Product
class AdminMenu():
    @staticmethod
    def option_choose():
        """
        This method will be called when admin is logged in
        and will be able to add or delete user or product
        """
        print("Choose your option 1 for user managment 2 for product managment q for quit")
        option = input("Enter your option: ")
        if option == "1":
            "Add or delete user"
            add_or_del = input("add or del user")
            if add_or_del == "add":
                Users.add_user()
                Users.add_adress_manualy()
            elif add_or_del == "del":
                Users.delete_user_by_id()
            else:
                print("Wrong option")
                AdminMenu.option_choose()

        elif option == "2":
            add_or_del = input("add or del product")
            if add_or_del == "add":
                Product.add_product()
            elif add_or_del == "del":
                Product.delete_product_by_id()
        elif option == "q":
            exit()
        else:
            print("Wrong option")
            AdminMenu.option_choose()

    @staticmethod
    def add_adress_manulay():
        street = input("Enter street: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter ZIP code: ")
        user_id = input("Enter user id: ")
        conn = BaseModel.cone_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO addresses (user_id, street, city, state, zip_code) 
            VALUES (%s, %s, %s, %s, %s)
            """,
            (user_id, street, city, state, zip_code)
        )