import pytest


# DEMO
def test_login_failure(login_page):
    login_page.navigate()
    login_page.login('user', 'password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username, password)
    dashboard_page.assert_welcome_message(f"Welcome {username}")
