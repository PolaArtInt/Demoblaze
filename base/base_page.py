import allure
from playwright.sync_api import Page, expect


class BasePage:
    URL = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open Page URL')
    def visit(self):
        if self.URL:
            self.page.goto(self.URL)
        else:
            print('Page URL not found. Please, check the page URL')

    def find_element(self, selector):
        return self.page.locator(selector)
