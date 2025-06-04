import allure
from playwright.sync_api import Page, expect, Dialog

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestCartPage:

    @allure.feature('Cart Page')
    @allure.title('Verify that cart page elements are displayed')
    def test_check_page_opened(self, cart_page: CartPage):
        cart_page.visit()
        expect(cart_page.cart_page_title(), "Wrong page title").to_have_text('Products')
        expect(cart_page.cart_page_total(), "Wrong text").to_have_text('Total')
        expect(cart_page.cart_page_table(), "The element is not present on the page").to_be_visible()
        expect(cart_page.cart_page_place_order_btn(), "The button is not present on the page").to_be_visible()

    @allure.feature('Cart Page')
    @allure.title('Test adding a random item to the cart without authentication')
    def test_item_added_to_cart(self, home_page: HomePage, product_page: ProductPage, cart_page: CartPage):
        home_page.visit()
        expect(home_page.all_items()).to_have_count(9)
        home_page.pick_random_item_link().click()

        expected_alert_message = 'Product added'
        actual_alert_message = product_page.click_add_to_cart_and_get_alert_message()
        assert actual_alert_message == expected_alert_message, \
            f"Unexpected alert message. Expected: '{expected_alert_message}', Actual: '{actual_alert_message}'"

        expect(product_page.product_title()).to_be_visible()
        saved_title = product_page.product_title().inner_text()

        cart_page.visit()
        expect(cart_page.cart_page_title()).to_be_visible()
        expect(cart_page.cart_page_title(), "Wrong page title").to_have_text('Products')

        actual_title = cart_page.cart_product_title().inner_text()
        assert saved_title == actual_title, \
            f"Unexpected product title. Expected: '{saved_title}', Actual: '{actual_title}'"

        expect(cart_page.delete_btn()).to_be_visible()
        cart_page.delete_btn().click()
        expect(cart_page.cart_product_title()).not_to_be_visible()
        expect(cart_page.cart_product()).not_to_be_visible()
