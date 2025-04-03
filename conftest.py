import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# DEMO
@pytest.fixture
def login_page(page):
    return LoginPage(page)


# DEMO
@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
