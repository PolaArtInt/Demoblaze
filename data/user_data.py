from faker import Faker
import time

fake = Faker()


class Data:
    @staticmethod
    def generate_user_data():
        body = {
            "userName": '_'.join(fake.name().split()),
            "password": fake.password()
        }
        return body


class UserPola:
    @staticmethod
    def fill_username():
        return "Pola2"

    @staticmethod
    def fill_password():
        return "123"


class UserSignUp:
    @staticmethod
    def fill_signup_username():
        # Add timestamp to ensure uniqueness
        timestamp = str(int(time.time()))
        username = f"{fake.user_name()}_{timestamp}"
        return username

    @staticmethod
    def fill_signup_password():
        password = fake.password()
        return password
