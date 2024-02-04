import allure
from locators.forgot_pass_page_locator import ForgotPageLocators
from data import ConstantData
from pages.base_page import BasePage


class LoginPageHelper(BasePage):
    @allure.step("Работа со страницей восстановления пароля. Нажатие на ссылку Восстановить пароль")
    def click_reset_password_link(self):
        self.go_to_page(ConstantData.AUTH_URL)
        self.find_element(ForgotPageLocators.RECOVER_PASSWORD).click()
