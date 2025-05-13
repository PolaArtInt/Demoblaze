from pages.cart_page import *


class TestCartPage:
    def test_check_page_opened(self, cart_page):
        cart_page.visit()
        expect(cart_page.CART_PAGE_TITLE, "Wrong page title").to_contain_text('Products')
        expect(cart_page.CART_PAGE_TOTAL, "Wrong text").to_contain_text('Total')
        expect(cart_page.CART_PAGE_TABLE, "The element is not present on the page").to_be_visible()
        expect(cart_page.PLACE_ORDER_BUTTON, "The button is not present on the page").to_be_visible()
