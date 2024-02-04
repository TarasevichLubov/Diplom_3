import time
import allure
from data import ConstantData
from pages.main_page import MainPageHelper
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет».")
    @allure.description("Тестирование, что осуществляется переход в личный кабинет.")
    def test_button_click_account(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.click_account_button()
        current_url = main_page.current_url()
        assert current_url == "https://stellarburgers.nomoreparties.site/login"

    @allure.title("Переход по клику на «История заказо».")
    @allure.description("Тестирование, что осуществляется переход в раздел «История заказов».")
    def test_history_of_orders(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.user_login()
        button_orders = main_page.find_element(MainPageLocators.BUTTON_ORDER_REGISTER).text
        assert button_orders == 'Оформить заказ'

    @allure.title("Переход по клику на «Выход».")
    @allure.description("Тестирование, что осуществляется выход из аккаунта.")
    def test_exit_from_account(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        time.sleep(3)
        main_page.user_login()
        time.sleep(3)
        main_page.click_account_button()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((MainPageLocators.BUTTON_EXIT)))
        time.sleep(3)
        main_page.find_element(MainPageLocators.BUTTON_EXIT).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((MainPageLocators.ENTER_BUTTON)))
        current_url = main_page.current_url()
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
