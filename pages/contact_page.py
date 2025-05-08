from playwright.sync_api import Page, expect

from base.base_page import BasePage


class ContactPage(BasePage):
    URL = 'https://www.demoblaze.com'

    def __init__(self, page: Page):
        super().__init__(page)
