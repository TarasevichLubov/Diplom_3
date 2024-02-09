import allure
from locators.forgot_pass_page_locator import ForgotPageLocators
from locators.login_page_locators import LoginPageLocators
from data import ConstantData, TestData
from pages.base_page import BasePage


class LoginPageHelper(BasePage):
    @allure.step("Работа со страницей восстановления пароля. Нажатие на ссылку Восстановить пароль")
    def click_reset_password_link(self):
        self.go_to_page(ConstantData.AUTH_URL)
        self.find_element(ForgotPageLocators.RECOVER_PASSWORD).click()

    @allure.step("Авторизация пользователя")
    def user_login(self):
        self.find_element(LoginPageLocators.EMAIL_ACCOUNT).send_keys(TestData.e_mail)
        self.find_element(LoginPageLocators.PASS_ACCOUNT).send_keys(TestData.passwd)
        self.find_element(LoginPageLocators.ENTER_BUTTON).click()
        self.wait_login_user()

    @allure.step("Ожидание входа пользователя")
    def wait_login_user(self):
        self.wait_element_invisible(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Ожидание загрузки страницы")
    def wait_enter_button(self):
        self.wait_element_visible(LoginPageLocators.ENTER_BUTTON)


