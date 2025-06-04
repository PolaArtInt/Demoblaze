import allure
from playwright.sync_api import Page, expect, Dialog

from base.base_page import BasePage


class AboutPage(BasePage):
    URL = 'https://www.demoblaze.com'

    ABOUT_LINK = '//a[normalize-space()="About us"]'

    def about_link(self):
        return self.find_element(self.ABOUT_LINK)

    # @allure.step("Open About us modal")
    # def open_about_modal(self):
    #     expect(self.about_link()).to_be_visible()
    #     self.find_element(self.about_link()).click()
