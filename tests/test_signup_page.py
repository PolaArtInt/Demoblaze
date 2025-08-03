import allure
import pytest
from playwright.sync_api import Page, expect, Dialog

import data.user_data
from pages.signup_page import SignupPage
from pages.login_page import LoginPage


class TestSignupPage:
    # List of tuples: (locator for button, descriptive button name)
    BUTTONS_TO_TEST = [
        (SignupPage.SIGNUP_X_BTN, 'X button'),
        (SignupPage.SIGNUP_CLOSE_BTN, 'Close button')
    ]
    @pytest.mark.parametrize("button_locator, button_name", BUTTONS_TO_TEST)
    @allure.feature('Sign up')
    @allure.title('Close Sign up modal by clicking on different buttons')
    def test_close_signup_modal_by_various_buttons(self, signup_page: SignupPage, button_locator, button_name):
        signup_page.visit()
        signup_page.open_signup_modal()
        expect(signup_page.signup_modal(), "Sign up modal should be visible after opening").to_be_visible()
        signup_page.close_signup_modal(button_locator, button_name)
        expect(signup_page.signup_modal(), "Sign up modal should not be visible after closing").not_to_be_visible()

    @allure.feature('Sign up')
    @allure.title('Sign up and then login as a newly created user')
    def test_signup(self, login_page: LoginPage, signup_page: SignupPage):
        # Generate credentials once
        sign_up_username = data.user_data.UserSignUp.fill_signup_username()
        sign_up_password = data.user_data.UserSignUp.fill_signup_password()

        # Sign up with stored credentials
        signup_page.visit()
        signup_page.open_signup_modal()
        signup_page.signup(sign_up_username, sign_up_password)

        # Login with the same credentials
        login_page.open_login_modal()
        login_page.login(sign_up_username, sign_up_password)
        expect(login_page.logout_link(), "User is not logged in").to_be_visible()
