import allure
from selenium.webdriver.common.action_chains import ActionChains
from locators.order_page_locator import OrderPageLocators
from pages.base_page import BasePage
import time


class OrderPageHelper(BasePage):

    def click_order_button(self):
        self.find_element(OrderPageLocators.ORDER_CARD).click()

    def get_count_all_orders(self):
        return self.find_element(OrderPageLocators.ALL_ORDERS).get_property("textContent")

    def get_count_day_orders(self):
        return self.find_element(OrderPageLocators.DAY_ORDERS).get_property("textContent")

    def get_in_work_orders(self):
        orders = self.find_elements(OrderPageLocators.ORDER_READY)
        order_list = []
        for order in orders:
            order_list.append(order.text)
        return order_list

    def get_card_view_class(self):
        return self.find_element(OrderPageLocators.CARD_VIEW).get_attribute('class')

    def get_history_order(self):
        return self.find_elements(OrderPageLocators.HISTORY_ORDER)
