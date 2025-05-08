from pages.login_page import *


class TestLoginPage:
    def test_login(self, login_page):
        login_page.visit()
        login_page.login("Pola2", "123")
        expect(login_page.LOGOUT_LINK).to_be_visible()
