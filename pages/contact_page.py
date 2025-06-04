import allure
from playwright.sync_api import Page, expect, Dialog

from base.base_page import BasePage


class ContactPage(BasePage):
    URL = 'https://www.demoblaze.com'

    CONTACT_LINK = '//a[normalize-space()="Contact"]'

    def contact_link(self):
        return self.find_element(self.CONTACT_LINK)

    # @allure.step("Open Contact modal")
    # def open_contact_modal(self):
    #     expect(self.contact_link()).to_be_visible()
    #     self.contact_link().click()
