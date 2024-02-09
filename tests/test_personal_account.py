import allure
from data import ConstantData
from pages.main_page import MainPageHelper
from pages.account_page import AccountPageHelper
from pages.login_page import LoginPageHelper


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет».")
    @allure.description("Тестирование, что осуществляется переход в личный кабинет.")
    def test_button_click_account(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.click_account_button()
        login_page = LoginPageHelper(driver)
        current_url = login_page.current_url()
        assert current_url == ConstantData.AUTH_URL

    @allure.title("Переход по клику на «История заказов».")
    @allure.description("Тестирование, что осуществляется переход в раздел «История заказов».")
    def test_history_of_orders(self, driver):
        login_page = LoginPageHelper(driver)
        login_page.go_to_page(ConstantData.AUTH_URL)
        login_page.user_login()
        main_page = MainPageHelper(driver)
        main_page.click_account_button()
        account_page = AccountPageHelper(driver)
        account_page.history_order_click()
        current_url = account_page.current_url()
        assert current_url == ConstantData.HISTORY

    @allure.title("Переход по клику на «Выход».")
    @allure.description("Тестирование, что осуществляется выход из аккаунта.")
    def test_exit_from_account(self, driver):
        login_page = LoginPageHelper(driver)
        login_page.go_to_page(ConstantData.AUTH_URL)
        login_page.user_login()
        main_page = MainPageHelper(driver)
        main_page.wait_button_add_order_visible()
        main_page.click_account_button()
        account_page = AccountPageHelper(driver)
        account_page.exit_button_click()
        login_page.wait_enter_button()
        current_url = account_page.current_url()
        assert current_url == ConstantData.AUTH_URL
