from playwright.sync_api import Page

from base.base_page import BasePage


# DEMO
class LoginPageDemo(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login')
        self.error_message = page.locator('#errorAlert')

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()
