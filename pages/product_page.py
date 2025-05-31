from playwright.sync_api import Page, expect

from base.base_page import BasePage


class ProductPage(BasePage):
    URL = 'https://www.demoblaze.com/prod.html'

    PRODUCT_TITLE = '//h2[@class="name"]'
    ADD_TO_CART_BTN = '//a[contains(text(), "Add to cart")]'

    def product_title(self):
        return self.find_element(self.PRODUCT_TITLE)

    def add_to_cart_btn(self):
        return self.find_element(self.ADD_TO_CART_BTN)
