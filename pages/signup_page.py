import allure
from playwright.sync_api import Page, expect

from base.base_page import BasePage


class SignupPage(BasePage):
    URL = 'https://www.demoblaze.com'

    SIGNUP_LINK = '//a[@id="signin2"]'

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Open Signup modal")
    def open_signup_modal(self):
        self.find_element(self.SIGNUP_LINK).click()
