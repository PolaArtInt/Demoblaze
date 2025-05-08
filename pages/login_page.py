import pytest
import allure
from playwright.sync_api import Page, expect

from base.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://www.demoblaze.com'

    def __init__(self, page: Page):
        super().__init__(page)
        self.LOGIN_LINK = page.locator('//a[@id="login2"]')
        self.LOGOUT_LINK = page.locator('//a[@id="logout2"]')
        self.WELCOME_TEXT = page.locator('//a[@id="nameofuser"]"]')

        self.USERNAME_INPUT = page.locator('//input[@id="loginusername"]')
        self.PASSWORD_INPUT = page.locator('//input[@id="loginpassword"]')
        self.LOGIN_BTN = page.locator('//button[@onclick="logIn()"]')

    @allure.step("User login")
    def login(self, username, password):
        self.LOGIN_LINK.click()
        self.USERNAME_INPUT.fill(username)
        self.PASSWORD_INPUT.fill(password)
        self.LOGIN_BTN.click()
