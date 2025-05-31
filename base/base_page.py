import allure
from playwright.sync_api import sync_playwright, Page, expect


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

    def find_elements(self, selector):
        items = self.page.locator(selector).all()
        return items

    def await_element(self, selector):
        return self.page.wait_for_selector(selector)

    @staticmethod
    @allure.step('Create a random number based on the page items length')
    def rand_num(num) -> int:
        import random
        num = random.randint(0, num - 1)
        return num
