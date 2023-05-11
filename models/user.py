from models.base_model import BaseModel


class Users(BaseModel):
    @staticmethod
    def login_user(username, password):
        """
        This method will log in user or return False
        :param username:
        :param password:
        :return:
        """
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
        user_exists = cursor.fetchone()
        if user_exists:
            return user_exists
        else:
            return False

    @staticmethod
    def add_user():
        """
        this method will add user to DB
        :param name:
        :param email:
        :param username:
        :param password:
        :return:
        """
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        name = input('Enter your name: ')
        email = input('Enter your email: ')
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        cursor.execute('INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)', (name, email, username, password))
        conn.commit()
        return "User added successfully"

    @staticmethod
    def delete_user_by_id():
        """
        This method will delete user from DB

        """
        id = input("Enter user id to delete: ")
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (id,))
        conn.commit()
        return "User deleted successfully"
    @staticmethod
    def update_adress(login):
        street = input("Enter street: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter ZIP code: ")

        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        user_id = login[0]
        cursor.execute(
            """
            INSERT INTO addresses (user_id, street, city, state, zip_code) 
            VALUES (%s, %s, %s, %s, %s)
            """,
            (user_id, street, city, state, zip_code)
        )
    @staticmethod
    def add_adress_manualy():
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

    @staticmethod
    def see_all_users():
        """
        This method will see all users from DB
        :return:
        """
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return "done!"





