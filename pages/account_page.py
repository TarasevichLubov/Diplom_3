import allure
from locators.account_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPageHelper(BasePage):
    @allure.step("Просмотр Истории заказов")
    def history_order_click(self):
        return self.find_element(AccountPageLocators.HISTORY_BUTTON).click()

    @allure.step("Нажатие на кнопку Выход")
    def exit_button_click(self):
        return self.find_element(AccountPageLocators.BUTTON_EXIT).click()

    @allure.step("Просмотр Ленты заказов")
    def get_history_card(self):
        return self.find_elements(AccountPageLocators.HISTORY_CARD)
