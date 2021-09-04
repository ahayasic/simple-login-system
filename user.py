import re
import db

class UserManager:

    EMAIL_REGEX = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')

    def __is_email_invalid(self, email):
        if UserManager.EMAIL_REGEX.fullmatch(email):
            return False
        return True

    def __user_already_exists(self, email):
        results = db.manager.query(f"SELECT * FROM users WHERE email = '{email}'")

        if len(results) != 0:
            return True
        return False

    def create_user(self, first_name, last_name, email, password):
        if self.__is_email_invalid(email):
            print("Invalid email")
            return False

        if self.__user_already_exists(email):
            print("User already exists")
            return False

        db.manager.query(
            f"INSERT INTO users VALUES ('{first_name}', '{last_name}', '{email}', '{password}')"
        )
        return True

    def validade_login(self, email, password):
        results = db.manager.query(f"SELECT password FROM users WHERE email = '{email}'")

        if len(results) == 0:
            return False

        if results[0][0] == password:
            return True

        return False
