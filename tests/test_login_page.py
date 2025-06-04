import allure
from playwright.sync_api import Page, expect, Dialog

import data.user_data
from pages.login_page import LoginPage


class TestLoginPage:
    @allure.feature('Login')
    @allure.title('Login as an existing user')
    def test_login(self, login_page: LoginPage):
        login_page.visit()
        login_page.open_login_modal()
        login_page.login(data.user_data.UserPola.fill_username(), data.user_data.UserPola.fill_password())
        expect(login_page.logout_link(), 'User is not logged in').to_be_visible()
