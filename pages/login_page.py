import allure
from playwright.sync_api import Page, expect, Dialog

from base.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://www.demoblaze.com'

    LOGIN_LINK = '//a[@id="login2"]'
    LOGOUT_LINK = '//a[@id="logout2"]'
    WELCOME_TEXT = '//a[@id="nameofuser"]'
    LOGIN_MODAL = '//div[@id="logInModal"]'

    USERNAME_INPUT = '//input[@id="loginusername"]'
    PASSWORD_INPUT = '//input[@id="loginpassword"]'
    CLOSE_BTN = '//div[@id="logInModal"]//button[@class="btn btn-secondary"]'
    LOGIN_BTN = '//button[@onclick="logIn()"]'

    @allure.step("Find Login link")
    def login_link(self):
        return self.find_element(self.LOGIN_LINK)

    @allure.step("Find Logout link")
    def logout_link(self):
        return self.find_element(self.LOGOUT_LINK)
    
    def login_modal(self):
        return self.find_element(self.LOGIN_MODAL)
    
    def welcome_user_link(self):
        return self.find_element(self.WELCOME_TEXT)

    def username_input(self):
        return self.find_element(self.USERNAME_INPUT)

    def password_input(self):
        return self.find_element(self.PASSWORD_INPUT)

    def login_btn(self):
        return self.find_element(self.LOGIN_BTN)

    @allure.step("Open Login modal")
    def open_login_modal(self):
        expect(self.login_link()).to_be_visible()
        self.login_link().click()

    @allure.step("User login to the system:")
    def login(self, username, password):
        with allure.step("Fill in a username"):
            expect(self.username_input()).to_be_visible()
            self.username_input().fill(username)
        with allure.step("Fill in a password"):
            expect(self.password_input()).to_be_visible()
            self.password_input().fill(password)
        with allure.step("Click the Login Button"):
            expect(self.login_btn()).to_be_visible()
            self.login_btn().click()
