import pytest

from pages.about_page import AboutPage
from pages.cart_page import CartPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.signup_page import SignupPage

# from pages.login_page_demo import LoginPageDemo
# from pages.dashboard_page_demo import DashboardPageDemo


@pytest.fixture
def about_page(page):
    return AboutPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def contact_page(page):
    return ContactPage(page)


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)


# # DEMO
# @pytest.fixture
# def login_page_demo(page):
#     return LoginPageDemo(page)
#
#
# # DEMO
# @pytest.fixture
# def dashboard_page_demo(page):
#     return DashboardPageDemo(page)
