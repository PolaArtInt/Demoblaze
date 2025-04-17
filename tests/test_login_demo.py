import pytest
import allure


@allure.feature('Авторизация')
@allure.title('Авторизация с недействительными учетными данными')
def test_login_failure(login_page_demo):
    with allure.step('Открыть страницу авторизации'):
        login_page_demo.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page_demo.login('invalid_user', 'invalid_password')
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page_demo.get_error_message() == 'Invalid credentials. Please try again.'


@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page_demo, dashboard_page_demo, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page_demo.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page_demo.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page_demo.assert_welcome_message(f"Welcome {username}")


@allure.feature('Test')
@allure.title('Test')
def test_allure_results_url(login_page_demo):
    with allure.step('Test'):
        login_page_demo.navigate()
    with allure.step('Test'):
        login_page_demo.login('invalid_user', 'invalid_password')
    with allure.step('Test'):
        assert login_page_demo.get_error_message() == 'Invalid credentials. Please try again.'
