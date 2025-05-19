import data.user_data
from pages.login_page import *
from data.user_data import *


class TestLoginPage:
    def test_login(self, login_page):
        login_page.visit()
        login_page.open_login_modal()
        login_page.login(data.user_data.UserPola.fill_username(), data.user_data.UserPola.fill_password())
        expect(login_page.find_element(login_page.LOGOUT_LINK), "User is not logged in").to_be_visible()
