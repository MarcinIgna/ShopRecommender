from methods.user import UserMethods
from menu.admin_menu import AdminMenu
from menu.user_menu import UserMenu


login = UserMethods.get_login()
if login:
    if login[6] == True:
        AdminMenu.option_choose()
    else:
        UserMenu.option_for_acc(login)
else:
    UserMenu.option_for_not_user()



