import allure
from playwright.sync_api import Page, expect

from base.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://www.demoblaze.com'

    LOGIN_LINK = '//a[@id="login2"]'
    LOGOUT_LINK = '//a[@id="logout2"]'
    WELCOME_TEXT = '//a[@id="nameofuser"]"]'

    USERNAME_INPUT = '//input[@id="loginusername"]'
    PASSWORD_INPUT = '//input[@id="loginpassword"]'
    CLOSE_BTN = '//div[@id="logInModal"]//button[@class="btn btn-secondary"]'
    LOGIN_BTN = '//button[@onclick="logIn()"]'

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Open Login modal")
    def open_login_modal(self):
        self.find_element(self.LOGIN_LINK).click()

    @allure.step("Find Logout link")
    def logout_link(self):
        return self.find_element(self.LOGOUT_LINK)

    @allure.step("User login to the system:")
    def login(self, username, password):
        with allure.step("Fill in a username"):
            self.find_element(self.USERNAME_INPUT).fill(username)
        with allure.step("Fill in a password"):
            self.find_element(self.PASSWORD_INPUT).fill(password)
        with allure.step("Click the Login Button"):
            self.find_element(self.LOGIN_BTN).click()
