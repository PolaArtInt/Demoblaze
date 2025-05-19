from playwright.sync_api import Page, expect

from base.base_page import BasePage


class CartPage(BasePage):
    URL = 'https://www.demoblaze.com/cart.html'

    CART_PAGE_TITLE = '(//h2)[1]'
    CART_PAGE_TOTAL = '(//h2)[2]'
    CART_PAGE_TABLE = '//table'
    PLACE_ORDER_BUTTON = '//button[@data-target="#orderModal"]'

    def __init__(self, page: Page):
        super().__init__(page)
