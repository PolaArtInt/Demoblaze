from faker import Faker

fake = Faker()


class Data:
    @staticmethod
    def generate_user_data():
        body = {
            "userName": '_'.join(fake.name().split()),
            "password": fake.password()
        }
        return body
