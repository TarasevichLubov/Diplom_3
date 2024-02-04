import allure
from locators.forgot_pass_page_locator import ForgotPageLocators
from locators.reset_pass_page_locators import ResetPassPageLocators
from data import ConstantData
from pages.base_page import BasePage


class ResetPassPageHelper(BasePage):
    @allure.step("Ввод адреса для восстановления пароля.")
    def click_visible_pass(self):
        self.go_to_page(ConstantData.RESET_PASSWORD)
        self.find_element(ForgotPageLocators.RECOVER_PASSWORD_BUTTON).click()
        self.find_element(ResetPassPageLocators.VISIBLE_PASS).click()
        selected_class = self.find_element(ResetPassPageLocators.VIEW_PASSWORD).get_attribute('class')
        return selected_class
