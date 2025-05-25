import data.user_data
from pages.signup_page import *
from pages.login_page import *


class TestSignupPage:
    @staticmethod
    def _close_signup_modal(signup_page, close_method):
        signup_page.visit()
        signup_page.open_signup_modal()
        expect(signup_page.signup_modal(), "Sign up modal is not open").to_be_visible()

        # Call the closing method passed as argument
        getattr(signup_page, close_method)()

        expect(signup_page.signup_modal(), "Sign up modal was not closed").not_to_be_visible()

    @allure.feature('Sign up')
    @allure.title('Close sign up modal by clicking on x button')
    def test_close_signup_modal_by_x_btn(self, signup_page):
        self._close_signup_modal(signup_page, 'close_signup_modal_by_x_btn')

    @allure.feature('Sign up')
    @allure.title('Close sign up modal by clicking on Close button')
    def test_close_signup_modal_by_close_btn(self, signup_page):
        self._close_signup_modal(signup_page, 'close_signup_modal_by_close_btn')

    @allure.feature('Sign up')
    @allure.title('Sign up and then login as a newly created user')
    def test_signup(self, login_page, signup_page):
        # Generate credentials once
        sign_up_username = data.user_data.UserSignUp.fill_signup_username()
        sign_up_password = data.user_data.UserSignUp.fill_signup_password()

        # Signup with stored credentials
        signup_page.visit()
        signup_page.open_signup_modal()
        signup_page.signup(sign_up_username, sign_up_password)

        # Login with the same credentials
        login_page.open_login_modal()
        login_page.login(sign_up_username, sign_up_password)
        expect(login_page.logout_link(), "User is not logged in").to_be_visible()
