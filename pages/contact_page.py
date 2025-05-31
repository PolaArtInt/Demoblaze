import allure
from playwright.sync_api import Page, expect

from base.base_page import BasePage


class ContactPage(BasePage):
    URL = 'https://www.demoblaze.com'

    CONTACT_LINK = '//a[normalize-space()="Contact"]'

    @allure.step("Open Contact modal")
    def open_contact_modal(self):
        self.find_element(self.find_element(self.CONTACT_LINK)).click()
