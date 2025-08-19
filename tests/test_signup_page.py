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
        
        # Validate generated credentials
        assert sign_up_username, "Username should not be empty"
        assert sign_up_password, "Password should not be empty"
        assert len(sign_up_username) > 0, "Username should have at least 1 character"
        assert len(sign_up_password) > 0, "Password should have at least 1 character"

        # Sign up with stored credentials
        signup_page.visit()
        signup_page.open_signup_modal()
        expect(signup_page.signup_modal(), "Sign up modal should be visible before signup").to_be_visible()
        
        expected_signup_alert_message = 'Sign up successful.'
        actual_signup_alert_message = signup_page.signup(sign_up_username, sign_up_password)
        assert actual_signup_alert_message == expected_signup_alert_message, \
            f"Unexpected signup alert message. Expected: '{expected_signup_alert_message}', Actual: '{actual_signup_alert_message}'"
        
        expect(signup_page.signup_modal(), "Sign up modal should not be visible after successful signup").not_to_be_visible()

        # Login with the same credentials
        login_page.open_login_modal()
        expect(login_page.login_modal(), "Login modal should be visible before login").to_be_visible()
        login_page.login(sign_up_username, sign_up_password)
        expect(login_page.logout_link(), "User is not logged in").to_be_visible()
        
        # Validate successful login by checking user is properly authenticated
        actual_welcome_text = login_page.welcome_user_link().inner_text()
        expected_welcome_text = f"Welcome {sign_up_username}"
        assert expected_welcome_text in actual_welcome_text, \
            f"Welcome message should contain username. Expected: '{expected_welcome_text}', Actual: '{actual_welcome_text}'"
