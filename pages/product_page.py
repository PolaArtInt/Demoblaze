import allure
from playwright.sync_api import Page, expect, Dialog

from base.base_page import BasePage


class ProductPage(BasePage):
    URL = 'https://www.demoblaze.com/prod.html'

    PRODUCT_TITLE = '//h2[@class="name"]'
    ADD_TO_CART_BTN = '//a[contains(text(), "Add to cart")]'

    def product_title(self):
        return self.find_element(self.PRODUCT_TITLE)

    def add_to_cart_btn(self):
        return self.find_element(self.ADD_TO_CART_BTN)

    @allure.step("Add product to cart and get alert message")
    def click_add_to_cart_and_get_alert_message(self):
        expect(self.add_to_cart_btn()).to_be_visible(timeout=10000)
        with self.page.expect_event("dialog") as dialog_info:
            self.add_to_cart_btn().click()

        dialog = dialog_info.value
        alert_message = dialog.message
        dialog.accept()
        return alert_message
