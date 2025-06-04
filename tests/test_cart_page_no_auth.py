from pages.cart_page import *
from pages.home_page import *
from pages.product_page import *


class TestCartPage:
    def test_check_page_opened(self, cart_page):
        cart_page.visit()
        expect(cart_page.cart_page_title(), "Wrong page title").to_have_text('Products')
        expect(cart_page.cart_page_total(), "Wrong text").to_have_text('Total')
        expect(cart_page.cart_page_table(), "The element is not present on the page").to_be_visible()
        expect(cart_page.cart_page_place_order_btn(), "The button is not present on the page").to_be_visible()

    def test_item_added_to_cart(self, home_page, product_page, cart_page):
        home_page.visit()
        expect(home_page.all_items()).to_have_count(9)

        home_page.pick_random_item().click()
        saved_title = product_page.product_title().inner_text()

        product_page.add_to_cart_btn().click()

        cart_page.visit()
        expect(cart_page.cart_page_title(), "Wrong page title").to_have_text('Products')

        expected_title = cart_page.cart_product_title().text_content()

        if '\n' in expected_title:
            expected_title.replace('\n', '')

        assert expected_title == saved_title, 'Wrong product'

        cart_page.delete_btn().click()
