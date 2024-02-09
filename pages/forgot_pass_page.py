import allure
from locators.forgot_pass_page_locator import ForgotPageLocators
from data import ConstantData, TestData
from pages.base_page import BasePage


class ForgotPassPageHelper(BasePage):
    @allure.step("Ввод адреса для восстановления пароля.")
    def enter_email_for_reset_pass(self):
        self.go_to_page(ConstantData.FORGOT_PASSWORD)
        self.wait_form_forgot_pass_load()
        self.find_element(ForgotPageLocators.EMAIL_RECOVER).send_keys(TestData.e_mail)
        self.find_element(ForgotPageLocators.RECOVER_PASSWORD_BUTTON).click()

    @allure.step("Ожидание загрузки страницы для восстановления пароля")
    def wait_form_forgot_pass_load(self):
        self.wait_element_visible(ForgotPageLocators.RECOVER_PASSWORD_BUTTON)


