from models.base_model import BaseModel
from models.user import Users
from models.product import Product
from models.recomendation import get_user_recommendations
class UserMenu():
    @staticmethod
    def option_for_acc(login):
        """
        This method will be called when user is logged in
        and will be able to change password or email
        """
        print(f"Welcome to your account {login[1]}!")
        # Get recommendations for user with ID
        recommendations = get_user_recommendations(login[0])
        print("Here are some recommendations for you:")
        print(recommendations.to_string(index=False))
        print("Choose 1 to see product 2 to manage your account q for quit")
        option_acc = input("Enter your option: ")
        if option_acc == "1":
            product_option = input(f"Choose 1 to see all products \n"
                                   f"2 to see product by category\n "
                                   f"3 to search by name\n "
                                   f"q for quit")
            if product_option == "1":
                Product.see_all_products()
            elif product_option == "2":
                Product.select_by_category()
            elif product_option == "q":
                exit()
            elif product_option == "3":
                product_name = Product.search_by_name()
                order_option = input("Choose 1 to order product q for quit") # in furure will be added to cart
                if order_option == "1":
                    print(Product.add_to_orders(product_name, login[0]))
                elif order_option == "q":
                    exit()
                else:
                    print("Wrong option")
                    UserMenu.option_for_acc(login)
            else:
                print("Wrong option")
                UserMenu.option_for_acc(login)
        elif option_acc == "2":
            print("Choose your option 1 for change password 2 for change email 3 for update address q for quit")
            option = input("Enter your option: ")
            if option == "1":
                conn = BaseModel.cone_db()
                cursor = conn.cursor()
                pass_input = input("Enter your password: ")
                cursor.execute('UPDATE users SET password = %s WHERE id = %s', (pass_input, login[0]))
                conn.commit()
                cursor.close()
                conn.close()
                print("Password changed successfully")
            elif option == "2":
                conn = BaseModel.cone_db()
                cursor = conn.cursor()
                email_input = input("Enter your email: ")
                cursor.execute('UPDATE users SET email = %s WHERE id = %s', (email_input, login[0]))
                conn.commit()
                cursor.close()
                conn.close()
            elif option == "3":
                Users.update_adress(login)
                exit()
            elif option == "q":
                exit()
            else:
                print("Wrong option")
                UserMenu.option_for_acc()
    @staticmethod
    def option_for_not_user():
        """
        This method will be called when user is not logged in
        and will be able to create account or login
        :return:
        """
        print("Choose your option 1 for create account q for quit")
        option = input("Enter your option: ")
        if option == "1":
            # Create a cursor object to execute SQL queries
            conn = BaseModel.cone_db()
            cursor = conn.cursor()

            # Prompt the user for the new user data
            name = input("Enter name: ")
            email = input("Enter email: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            street = input("Enter street: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            zip_code = input("Enter ZIP code: ")

            # Insert a new row into the "users" table
            cursor.execute(
                """
                INSERT INTO users (name, email, username, password, registration_date, is_admin) 
                VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, false)
                RETURNING id
                """,
                (name, email, username, password)
            )

            # Fetch the generated user ID
            user_id = cursor.fetchone()[0]

            # Insert a new row into the "addresses" table
            cursor.execute(
                """
                INSERT INTO addresses (user_id, street, city, state, zip_code) 
                VALUES (%s, %s, %s, %s, %s)
                """,
                (user_id, street, city, state, zip_code)
            )

            # Commit the changes to the database
            conn.commit()

            # Close the cursor and the database connection
            cursor.close()
            conn.close()

            print("New user and address added successfully")
        elif option == "q":
            exit()
        else:
            print("Wrong option")
            UserMenu.option_for_not_user()

