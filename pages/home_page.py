import allure
from playwright.sync_api import Page, expect, Dialog

from base.base_page import BasePage


class HomePage(BasePage):
    URL = 'https://www.demoblaze.com'

    ALL_ITEM_LINKS = '//div[@id="tbodyid"]//h4[@class="card-title"]/a'
    ITEM_TITLES = '//div[@id="tbodyid"]//h4[@class="card-title"]'

    @allure.step('Get all item links on the Home Page')
    def all_items(self):
        return self.find_elements(self.ALL_ITEM_LINKS)

    @allure.step('Pick a random item from the Home Page')
    def pick_random_item_link(self):
        expect(self.all_items().first).to_be_visible(timeout=10000)

        all_item_locators = self.all_items().all()
        random_index = self.rand_num(len(all_item_locators))
        selected_item_locator = all_item_locators[random_index]

        expect(selected_item_locator).to_be_visible()
        expect(selected_item_locator).to_be_enabled()

        return selected_item_locator
