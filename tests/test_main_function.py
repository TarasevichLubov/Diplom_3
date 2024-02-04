import allure
import time
from data import ConstantData
from pages.main_page import MainPageHelper
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMainFunction:
    @allure.title("Переход по клику на «Конструктор».")
    @allure.description("Тестирование, что осуществляется переход на вкладку Конструктор.")
    def test_click_burger_builder(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        time.sleep(3)
        main_page.click_orders_button()
        time.sleep(3)
        main_page.click_designer_button()
        selected_class = main_page.find_element(MainPageLocators.DESIGNER_BUTTON).get_attribute('class')
        assert 'link_active' in selected_class

    @allure.title("Переход по клику на «Лента заказов».")
    @allure.description("Тестирование, что осуществляется переход на вкладку Лента заказов.")
    def test_click_order_builder(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        time.sleep(3)
        main_page.click_orders_button()
        time.sleep(3)
        selected_class = main_page.find_element(MainPageLocators.ORDER_BUTTON).get_attribute('class')
        assert 'link_active' in selected_class

    @allure.title("Переход в детальное окно ингредиента.")
    @allure.description("Тестирование, что, если кликнуть на ингредиент, появится всплывающее окно с деталями.")
    def test_burger_window(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        time.sleep(3)
        main_page.click_orders_card()
        time.sleep(3)
        selected_class = main_page.find_element(MainPageLocators.CARD_INGREDIENT).get_attribute('class')
        assert 'modal_opened' in selected_class

    @allure.title("Закрытие окна детального просмотра ингредиента.")
    @allure.description("Тестирование, что всплывающее окно закрывается кликом по крестику.")
    def test_close_card(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        time.sleep(3)
        main_page.click_orders_card()
        time.sleep(3)
        main_page.close_card_click()
        selected_class = main_page.find_element(MainPageLocators.CARD_INGREDIENT).get_attribute('class')
        assert 'modal_opened' not in selected_class

    @allure.title("Добавление ингредиента в заказ.")
    @allure.description("Тестирование, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.")
    def test_add_order(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        count = main_page.find_element(MainPageLocators.INGREDIENT_COUNT).get_property("textContent")
        time.sleep(3)
        main_page.drag_and_drop(MainPageLocators.CARDS_LOCATOR, MainPageLocators.ORDER_ADD)
        time.sleep(3)
        new_count = main_page.find_element(MainPageLocators.INGREDIENT_COUNT, 5).get_property("textContent")
        assert int(new_count) == int(count) + 2

    @allure.title("Оформление заказа залогиненный пользователем.")
    @allure.description("Тестирование, что залогиненный пользователь может оформить заказ.")
    def test_login_user_order(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.user_login()
        time.sleep(3)
        main_page.drag_and_drop(MainPageLocators.CARDS_LOCATOR, MainPageLocators.ORDER_ADD)
        time.sleep(3)
        main_page.click_orders_register()
        wait = WebDriverWait(driver, 10)
        wait.until_not(expected_conditions.text_to_be_present_in_element(MainPageLocators.ORDER_ID, '9999'))
        id_order = main_page.find_element(MainPageLocators.ORDER_ID).get_property("textContent")
        time.sleep(3)
        assert id_order != '9999'
