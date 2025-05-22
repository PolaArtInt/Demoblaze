from pages.cart_page import *


class TestCartPage:
    def test_check_page_opened(self, cart_page):
        cart_page.visit()
        expect(cart_page.cart_page_title(), "Wrong page title").to_have_text('Products')
        expect(cart_page.cart_page_total(), "Wrong text").to_have_text('Total')
        expect(cart_page.cart_page_table(), "The element is not present on the page").to_be_visible()
        expect(cart_page.cart_page_place_order_btn(), "The button is not present on the page").to_be_visible()
