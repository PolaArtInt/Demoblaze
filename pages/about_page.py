import allure
from playwright.sync_api import Page, expect

from base.base_page import BasePage


class AboutPage(BasePage):
    URL = 'https://www.demoblaze.com'

    ABOUT_LINK = '//a[normalize-space()="About us"]'

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Open About us modal")
    def open_about_modal(self):
        self.find_element(self.ABOUT_LINK).click()
