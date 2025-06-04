import allure
from playwright.sync_api import Page, expect, Dialog

from base.base_page import BasePage


class SignupPage(BasePage):
    URL = 'https://www.demoblaze.com'

    SIGNUP_LINK = '//a[@id="signin2"]'
    SIGNUP_MODAL = '//div[@id="signInModal"]'
    SIGNUP_X_BTN = '//div[@id="signInModal"]//span[@aria-hidden="true"][normalize-space()="×"]'
    SIGNUP_CLOSE_BTN = '//div[@id="signInModal"]//button[@type="button"][normalize-space()="Close"]'
    SIGNUP_USERNAME_FIELD = '#sign-username'
    SIGNUP_PASSWORD_FIELD = '#sign-password'
    SIGNUP_BTN = '//button[normalize-space()="Sign up"]'

    @allure.step("Open Sign up modal")
    def open_signup_modal(self):
        self.find_element(self.SIGNUP_LINK).click()

    @allure.step("Locate Sign up modal")
    def signup_modal(self):
        return self.find_element(self.SIGNUP_MODAL)

    @allure.step("Close Sign up modal by clicking on the x button")
    def close_signup_modal_by_x_btn(self):
        self.find_element(self.SIGNUP_X_BTN).click()

    @allure.step("Close Sign up modal by clicking on the Close button")
    def close_signup_modal_by_close_btn(self):
        self.find_element(self.SIGNUP_CLOSE_BTN).click()

    @allure.step("User signs up:")
    def signup(self, username, password):
        with allure.step("Fill in a username"):
            self.find_element(self.SIGNUP_USERNAME_FIELD).fill(username)
        with allure.step("Fill in a password"):
            self.find_element(self.SIGNUP_PASSWORD_FIELD).fill(password)
        with allure.step("Click the Sign up button"):
            self.find_element(self.SIGNUP_BTN).click()

    # К рассмотрению:
    # def signup_link(self):
    #     return self.find_element(self.SIGNUP_LINK)
    #
    # def signup_modal(self):
    #     return self.find_element(self.SIGNUP_MODAL)
    #
    # def signup_x_btn(self):
    #     return self.find_element(self.SIGNUP_X_BTN)
    #
    # def signup_close_btn(self):
    #     return self.find_element(self.SIGNUP_CLOSE_BTN)
    #
    # def signup_username_field(self):
    #     return self.find_element(self.SIGNUP_USERNAME_FIELD)
    #
    # def signup_password_field(self):
    #     return self.find_element(self.SIGNUP_PASSWORD_FIELD)
    #
    # def signup_button(self):
    #     return self.find_element(self.SIGNUP_BTN)
    #
    # @allure.step("Open Sign up modal")
    # def open_signup_modal(self):
    #     expect(self.signup_link()).to_be_visible()
    #     self.signup_link().click()
    #
    # @allure.step("Locate Sign up modal")
    # def signup_modal(self):
    #     expect(self.signup_modal()).to_be_visible()
    #     return self.find_element(self.signup_modal())
    #
    # @allure.step("Close Sign up modal by clicking on the x button")
    # def close_signup_modal_by_x_btn(self):
    #     expect(self.signup_x_btn()).to_be_visible()
    #     self.signup_x_btn().click()
    #
    # @allure.step("Close Sign up modal by clicking on the Close button")
    # def close_signup_modal_by_close_btn(self):
    #     expect(self.signup_close_btn()).to_be_visible()
    #     self.signup_close_btn().click()
    #
    # @allure.step("User signs up:")
    # def signup(self, username, password):
    #     with allure.step("Fill in a username"):
    #         expect(self.signup_username_field()).to_be_visible()
    #         self.find_element(self.signup_username_field()).fill(username)
    #     with allure.step("Fill in a password"):
    #         expect(self.signup_password_field()).to_be_visible()
    #         self.signup_password_field().fill(password)
    #     with allure.step("Click the Sign up button"):
    #         expect(self.signup_button()).to_be_visible()
    #         self.signup_button().click()
