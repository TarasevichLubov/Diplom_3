import allure
from data import ConstantData
from pages.login_page import LoginPageHelper
from pages.forgot_pass_page import ForgotPassPageHelper
from pages.reset_pass_page import ResetPassPageHelper


class TestRecover:

    @allure.title("Переход по клику на «Восстановить пароль».")
    @allure.description("Тестирование, что осуществляется переход на страницу "
                        "восстановления пароля по кнопке «Восстановить пароль».")
    def test_recover_password_link(self, driver):
        login_page = LoginPageHelper(driver)
        login_page.click_reset_password_link()
        forgot_pass_page = ForgotPassPageHelper(driver)
        forgot_pass_page.wait_form_forgot_pass_load()
        assert forgot_pass_page.current_url() == ConstantData.FORGOT_PASSWORD

    @allure.title("Ввод почты и клик по кнопке «Восстановить»,")
    @allure.description("Тестирование, ввод почты и клик по кнопке «Восстановить».")
    def test_email_enter_in_recover_link(self, driver):
        forgot_pass_page = ForgotPassPageHelper(driver)
        forgot_pass_page.enter_email_for_reset_pass()
        reset_pass_page = ResetPassPageHelper(driver)
        reset_pass_page.wait_form_reset_pass_load()
        assert reset_pass_page.current_url() == ConstantData.RESET_PASSWORD

    @allure.title("Клик по кнопке показать/скрыть пароль.")
    @allure.description("Тестирование клика по кнопке показать/скрыть пароль.")
    def test_click_visible_password(self, driver):
        forgot_pass_page = ForgotPassPageHelper(driver)
        forgot_pass_page.enter_email_for_reset_pass()
        reset_pass_page = ResetPassPageHelper(driver)
        reset_pass_page.wait_form_reset_pass_load()
        selected_class = reset_pass_page.click_visible_pass()
        assert 'focused' in selected_class
