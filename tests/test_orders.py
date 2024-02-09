import allure
from data import ConstantData
from pages.order_page import OrderPageHelper
from pages.login_page import LoginPageHelper
from pages.account_page import AccountPageHelper
from pages.main_page import MainPageHelper


class TestOrders:

    @allure.title("Всплывающее окно с деталями заказа.")
    @allure.description("Тестирование, если кликнуть на заказ, откроется всплывающее окно с деталями.")
    def test_order_click(self, driver):
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        order_page.click_order_button()
        selected_class = order_page.get_card_view_class()
        assert 'modal_opened' in selected_class

    @allure.title("Тестирование Ленты заказов.")
    @allure.description("Тестирование, что заказы пользователя из раздела «История заказов» "
                        "отображаются на странице «Лента заказов».")
    def test_include_orders(self, driver):
        login_page = LoginPageHelper(driver)
        login_page.go_to_page(ConstantData.AUTH_URL)
        login_page.user_login()
        main_page = MainPageHelper(driver)
        main_page.wait_button_add_order_visible()
        main_page.click_account_button()
        account_page = AccountPageHelper(driver)
        account_page.history_order_click()
        cards = account_page.get_history_card()
        card_list = account_page.get_list_element(cards)
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        history = order_page.get_history_order()
        history_list = order_page.get_list_element(history)
        check_order = order_page.check_orders_in_history(card_list, history_list)

        assert check_order == len(card_list)

    @allure.title("Тестирование счетчика заказа.")
    @allure.description("Тестирование, что при создании нового заказа счётчик Выполнено за всё время увеличивается.")
    def test_count_all_orders(self, driver):
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        count_all_orders = int(order_page.get_count_all_orders())
        login_page = LoginPageHelper(driver)
        login_page.go_to_page(ConstantData.AUTH_URL)
        login_page.user_login()
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_add_order_visible()
        main_page.add_ingredient_in_order()
        main_page.wait_num_order()
        main_page.click_orders_register()
        main_page.wait_all_num_order()
        new_count = int(main_page.get_all_orders_count())
        assert count_all_orders+1 == new_count

    @allure.title("Тестирование счетчика заказа.")
    @allure.description("Тестирование, что при создании нового заказа счётчик Выполнено за сегодня увеличивается.")
    def test_count_days_orders(self, driver):
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        count_all_orders = int(order_page.get_count_day_orders())
        login_page = LoginPageHelper(driver)
        login_page.go_to_page(ConstantData.AUTH_URL)
        login_page.user_login()
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_add_order_visible()
        main_page.add_ingredient_in_order()
        main_page.wait_num_order()
        main_page.click_orders_register()
        main_page.wait_all_num_order()
        main_page.close_card_click()
        order_page.go_to_page(ConstantData.ORDER)
        new_count_all_orders = int(order_page.get_count_day_orders())
        assert count_all_orders < new_count_all_orders

    @allure.title("Тестирование счетчика заказа.")
    @allure.description("Тестирование, что после оформления заказа его номер появляется в разделе В работе.")
    def test_in_work(self, driver):
        login_page = LoginPageHelper(driver)
        login_page.go_to_page(ConstantData.AUTH_URL)
        login_page.user_login()
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_add_order_visible()
        main_page.add_ingredient_in_order()
        main_page.wait_num_order()
        main_page.click_orders_register()
        id_order = main_page.get_all_orders_count()
        main_page.close_card_click()
        order_page = OrderPageHelper(driver)
        order_page.go_to_page(ConstantData.ORDER)
        order_page.wait_all_orders()
        order_list = order_page.get_in_work_orders()
        assert id_order in order_list
