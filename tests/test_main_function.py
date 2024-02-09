import allure
from data import ConstantData
from pages.main_page import MainPageHelper
from pages.login_page import LoginPageHelper


class TestMainFunction:
    @allure.title("Переход по клику на «Конструктор».")
    @allure.description("Тестирование, что осуществляется переход на вкладку Конструктор.")
    def test_click_burger_builder(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_enter_account_visible()
        main_page.click_orders_button()
        main_page.click_designer_button()
        selected_class = main_page.get_selected_class_designer()
        assert 'link_active' in selected_class

    @allure.title("Переход по клику на «Лента заказов».")
    @allure.description("Тестирование, что осуществляется переход на вкладку Лента заказов.")
    def test_click_order_builder(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_enter_account_visible()
        main_page.click_orders_button()
        selected_class = main_page.get_selected_class_order()
        assert 'link_active' in selected_class

    @allure.title("Переход в детальное окно ингредиента.")
    @allure.description("Тестирование, что, если кликнуть на ингредиент, появится всплывающее окно с деталями.")
    def test_burger_window(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_enter_account_visible()
        main_page.click_orders_card()
        selected_class = main_page.get_selected_class_ingredient()
        assert 'modal_opened' in selected_class

    @allure.title("Закрытие окна детального просмотра ингредиента.")
    @allure.description("Тестирование, что всплывающее окно закрывается кликом по крестику.")
    def test_close_card(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_enter_account_visible()
        main_page.click_orders_card()
        main_page.close_card_click()
        selected_class = main_page.get_selected_class_ingredient()
        assert 'modal_opened' not in selected_class

    @allure.title("Добавление ингредиента в заказ.")
    @allure.description("Тестирование, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.")
    def test_add_order(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page(ConstantData.BASE_URL)
        main_page.wait_button_enter_account_visible()
        count = main_page.get_count_ingredient()
        main_page.add_ingredient_in_order()
        main_page.wait_num_order()
        new_count = main_page.get_count_ingredient()
        assert int(new_count) == int(count) + 2

    @allure.title("Оформление заказа залогиненный пользователем.")
    @allure.description("Тестирование, что залогиненный пользователь может оформить заказ.")
    def test_login_user_order(self, driver):
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
        id_order = main_page.get_all_orders_count()
        assert id_order != '9999'
