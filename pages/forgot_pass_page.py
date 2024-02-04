import time

import allure
from locators.forgot_pass_page_locator import ForgotPageLocators
from data import ConstantData
from pages.base_page import BasePage


class ForgotPassPageHelper(BasePage):
    @allure.step("Ввод адреса для восстановления пароля.")
    def enter_email_for_reset_pass(self):
        self.go_to_page(ConstantData.FORGOT_PASSWORD)
        time.sleep(2)
        self.find_element(ForgotPageLocators.EMAIL_RECOVER, 10).send_keys(ConstantData.e_mail)
        self.find_element(ForgotPageLocators.RECOVER_PASSWORD_BUTTON, 10).click()


