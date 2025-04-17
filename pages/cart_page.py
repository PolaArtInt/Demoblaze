from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
