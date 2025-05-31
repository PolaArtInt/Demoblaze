from playwright.sync_api import Page, expect

from base.base_page import BasePage


class HomePage(BasePage):
    URL = 'https://www.demoblaze.com'

    ALL_ITEMS = '//h4[@class="card-title"]//a'
    ITEM_TITLE = '//h4[@class="card-title"]'

    def all_items(self):
        return self.find_element(self.ALL_ITEMS)

    def item_title(self):
        return self.find_element(self.ITEM_TITLE)

    def list_of_items(self):
        return self.find_elements(self.ALL_ITEMS)

    def items_list_length(self):
        return self.all_items().count()

    def pick_random_item(self):
        return self.list_of_items()[self.rand_num(self.items_list_length())]






