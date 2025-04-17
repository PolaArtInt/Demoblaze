from playwright.sync_api import Page, expect


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
