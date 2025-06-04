import allure
from playwright.sync_api import Page, expect, Dialog


class BasePage:
    URL = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open Page URL')
    def visit(self):
        if self.URL:
            # Используем wait_until='load' для более надежного ожидания загрузки страницы.
            # Это ждет, пока все основные ресурсы (CSS, JS, изображения) будут загружены.
            self.page.goto(self.URL, wait_until='load')
        else:
            print('Page URL not found. Please, check the page URL')

    def find_element(self, selector):
        return self.page.locator(selector)

    def find_elements(self, selector):
        # find_elements теперь возвращает Locator, на котором можно вызывать .count() или .all()
        return self.page.locator(selector)

    @allure.step('Wait for element to be visible: {selector}')
    def await_element_visible(self, selector):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        return locator

    @staticmethod
    @allure.step('Create a random number based on the page items length')
    def rand_num(num) -> int:
        import random
        num = random.randint(0, num - 1)
        return num
