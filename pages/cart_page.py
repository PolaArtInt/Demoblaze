from playwright.sync_api import Page, expect

from base.base_page import BasePage


class CartPage(BasePage):
    URL = 'https://www.demoblaze.com/cart.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.CART_PAGE_TITLE = page.locator('(//h2)[1]')
        self.CART_PAGE_TOTAL = page.locator('(//h2)[2]')
        self.CART_PAGE_TABLE = page.locator('//table')
        self.PLACE_ORDER_BUTTON = page.locator('//button[@data-target="#orderModal"]')
