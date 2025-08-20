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

    def signup_link(self):
        return self.find_element(self.SIGNUP_LINK)

    def signup_modal(self):
        return self.find_element(self.SIGNUP_MODAL)

    def signup_x_btn(self):
        return self.SIGNUP_X_BTN

    def signup_close_btn(self):
        return self.SIGNUP_CLOSE_BTN

    def signup_username_field(self):
        return self.find_element(self.SIGNUP_USERNAME_FIELD)

    def signup_password_field(self):
        return self.find_element(self.SIGNUP_PASSWORD_FIELD)

    def signup_button(self):
        return self.find_element(self.SIGNUP_BTN)

    @allure.step("Open Sign up modal")
    def open_signup_modal(self):
        expect(self.signup_link()).to_be_visible()
        self.signup_link().click()

    @allure.step("Close Sign up modal by clicking the '{button_name}'")
    def close_signup_modal(self, button_selector, button_name):
        expect(self.find_element(button_selector)).to_be_visible()
        self.find_element(button_selector).click()

    @allure.step("User signs up:")
    def signup(self, username, password):
        with allure.step("Fill in a username"):
            expect(self.signup_username_field()).to_be_visible()
            self.find_element(self.SIGNUP_USERNAME_FIELD).fill(username)
        with allure.step("Fill in a password"):
            expect(self.signup_password_field()).to_be_visible()
            self.find_element(self.SIGNUP_PASSWORD_FIELD).fill(password)
        with allure.step("Click the Sign up button and get alert message"):
            expect(self.signup_button()).to_be_visible()
            with self.page.expect_event("dialog") as dialog_info:
                self.find_element(self.SIGNUP_BTN).click()
            
            dialog = dialog_info.value
            alert_message = dialog.message
            dialog.accept()
            return alert_message
