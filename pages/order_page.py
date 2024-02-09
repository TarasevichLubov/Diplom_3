import allure
from locators.order_page_locator import OrderPageLocators
from pages.base_page import BasePage


class OrderPageHelper(BasePage):

    @allure.step("Нажатие на карточку заказа.")
    def click_order_button(self):
        self.find_element(OrderPageLocators.ORDER_CARD).click()

    @allure.step("Получение количества всех заказов.")
    def get_count_all_orders(self):
        return self.find_element(OrderPageLocators.ALL_ORDERS).get_property("textContent")

    @allure.step("Получение количества заказов за день.")
    def get_count_day_orders(self):
        return self.find_element(OrderPageLocators.DAY_ORDERS).get_property("textContent")

    @allure.step("Получение соответствующих заказов в общем списке заказов.")
    def get_in_work_orders(self):
        orders = self.find_elements(OrderPageLocators.ORDER_READY)
        order_list = []
        for order in orders:
            order_list.append(order.text)
        return order_list

    @allure.step("Просмотр заказа.")
    def get_card_view_class(self):
        return self.find_element(OrderPageLocators.CARD_VIEW).get_attribute('class')

    @allure.step("Проверка заказа.")
    def check_orders_in_history(self, card_list, history_list):
        check_order = 0
        for cards in card_list:
            if cards in history_list:
                check_order += 1
        return check_order

    @allure.step("Просмотр истории заказов.")
    def get_history_order(self):
        return self.find_elements(OrderPageLocators.HISTORY_ORDER)

    @allure.step("Ожидание исчезновения надписи.")
    def wait_all_orders(self):
        self.wait_text_to_be_visible(OrderPageLocators.ALL_ORDERS, 'Все текущие заказы готовы!')
