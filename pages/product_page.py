from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
