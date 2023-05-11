# Here we will have class with user methods what is not related to DB operations
from models.user import Users
# users
# login user

class UserMethods():
    @staticmethod
    def get_login():
        """
        This method will be called when user is not logged in
        :return:
        """
        # name = input("Enter your name: ")
        # password = input("Enter your password: ")
        name = "asmith"
        password = "password123"
        return Users.login_user(name, password)






