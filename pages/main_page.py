import allure
from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import ConstantData
import time


class MainPageHelper(BasePage):

    def click_account_button(self):
        self.find_element(MainPageLocators.ACCOUNT).click()

    def user_login(self):
        self.click_account_button()
        self.find_element(MainPageLocators.EMAIL_ACCOUNT).send_keys(ConstantData.e_mail)
        self.find_element(MainPageLocators.PASS_ACCOUNT).send_keys(ConstantData.passwd)
        self.find_element(MainPageLocators.ENTER_BUTTON).click()

    @allure.step("Переход по кнопке Конструктор")
    def click_designer_button(self):
        self.find_element(MainPageLocators.DESIGNER_BUTTON).click()

    def click_orders_button(self):
        self.find_element(MainPageLocators.ORDER_BUTTON).click()

    def click_orders_card(self):
        self.find_element(MainPageLocators.CARDS_LOCATOR).click()

    def click_orders_register(self):
        self.find_element(MainPageLocators.BUTTON_ORDER_REGISTER).click()

    def history_button_click(self):
        self.find_element(MainPageLocators.HISTORY_BUTTON).click()

    def get_card_element(self):
        self.find_element(MainPageLocators.CARD_INGREDIENT)

    def get_order_id(self):
        return self.find_element(MainPageLocators.ORDER_ID).get_property("textContent")

    def get_all_orders_count(self):
        return self.find_element(MainPageLocators.ORDER_ID).get_property("textContent")

    def close_card_click(self):
        self.find_element(MainPageLocators.CARD_CLOSE).click()

    def drag_and_drop(self, locator_1, locator_2):
        element = self.driver.find_element(*locator_1)
        target = self.driver.find_element(*locator_2)
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element, target).perform()
