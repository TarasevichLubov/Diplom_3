import time
import allure
from data import ConstantData
from pages.order_page import OrderPageHelper
from locators.order_page_locator import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPageHelper


class TestOrders:

    @allure.title("Всплывающее окно с деталями заказа.")
    @allure.description("Тестирование, если кликнуть на заказ, откроется всплывающее окно с деталями.")
    def test_order_click(self, driver):
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        time.sleep(3)
        order_page.click_order_button()
        time.sleep(3)
        selected_class = order_page.get_card_view_class()
        assert 'modal_opened' in selected_class

    @allure.title("Тестирование Ленты заказов.")
    @allure.description("Тестирование, что заказы пользователя из раздела «История заказов» "
                        "отображаются на странице «Лента заказов».")
    def test_include_orders(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.user_login()
        time.sleep(3)
        main_page.click_account_button()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((MainPageLocators.BUTTON_EXIT)))
        time.sleep(3)
        main_page.history_button_click()
        cards = main_page.find_elements(MainPageLocators.HISTORY_CARD)
        card_list = []
        for card in cards:
            card_list.append(card.text)
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        history = order_page.get_history_order()
        history_list = []
        for hr in history:
            history_list.append(hr.text)
        check_order = 0
        for cards in card_list:
            if cards in history_list:
                check_order += 1

        assert check_order == len(card_list)

    @allure.title("Тестирование счетчика заказа.")
    @allure.description("Тестирование, что при создании нового заказа счётчик Выполнено за всё время увеличивается.")
    def test_count_all_orders(self, driver):
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        count_all_orders = int(order_page.get_count_all_orders())
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.user_login()
        time.sleep(3)
        main_page.drag_and_drop(MainPageLocators.CARDS_LOCATOR, MainPageLocators.ORDER_ADD)
        time.sleep(3)
        main_page.click_orders_register()
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        wait.until_not(expected_conditions.text_to_be_present_in_element(OrderPageLocators.ALL_ORDERS, '9999'))
        new_count = int(main_page.get_all_orders_count())
        assert count_all_orders+1 == new_count

    @allure.title("Тестирование счетчика заказа.")
    @allure.description("Тестирование, что при создании нового заказа счётчик Выполнено за сегодня увеличивается.")
    def test_count_days_orders(self, driver):
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        count_all_orders = int(order_page.get_count_day_orders())
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.user_login()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((MainPageLocators.BUTTON_ORDER_REGISTER)))
        main_page.drag_and_drop(MainPageLocators.CARDS_LOCATOR, MainPageLocators.ORDER_ADD)
        main_page.click_orders_register()
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        wait.until_not(expected_conditions.text_to_be_present_in_element(OrderPageLocators.ALL_ORDERS, '9999'))
        order_page.go_to_page(ConstantData.ORDER)
        new_count_all_orders = int(order_page.get_count_day_orders())
        assert count_all_orders < new_count_all_orders

    @allure.title("Тестирование счетчика заказа.")
    @allure.description("Тестирование, что после оформления заказа его номер появляется в разделе В работе.")
    def test_in_work(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.user_login()
        time.sleep(3)
        main_page.drag_and_drop(MainPageLocators.CARDS_LOCATOR, MainPageLocators.ORDER_ADD)
        time.sleep(3)
        main_page.click_orders_register()
        wait = WebDriverWait(driver, 10)
        wait.until_not(expected_conditions.text_to_be_present_in_element(OrderPageLocators.ALL_ORDERS, '9999'))
        id_order = main_page.get_order_id()
        main_page.close_card_click()
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        time.sleep(3)
        wait = WebDriverWait(driver, 20)
        wait.until_not(expected_conditions.text_to_be_present_in_element(OrderPageLocators.ALL_ORDERS,
                                                                         'Все текущие заказы готовы!'))
        order_list = order_page.get_in_work_orders()
        assert id_order in order_list
