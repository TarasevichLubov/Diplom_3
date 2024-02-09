import allure
from locators.reset_pass_page_locators import ResetPassPageLocators
from pages.base_page import BasePage


class ResetPassPageHelper(BasePage):
    @allure.step("Ввод адреса для восстановления пароля.")
    def click_visible_pass(self):
        self.find_element(ResetPassPageLocators.VISIBLE_PASS).click()
        selected_class = self.find_element(ResetPassPageLocators.VIEW_PASSWORD).get_attribute('class')
        return selected_class

    @allure.step("Ожидание загрузки страницы для восстановления пароля")
    def wait_form_reset_pass_load(self):
        self.wait_element_visible(ResetPassPageLocators.SAVE_BUTTON)
