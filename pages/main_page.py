import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPageHelper(BasePage):

    @allure.step("Переход по кнопке Личный кабинет")
    def click_account_button(self):
        self.find_element(MainPageLocators.ACCOUNT).click()

    @allure.step("Переход по кнопке Конструктор")
    def click_designer_button(self):
        self.find_element(MainPageLocators.DESIGNER_BUTTON).click()

    @allure.step("Переход в ленту заказов")
    def click_orders_button(self):
        self.find_element(MainPageLocators.ORDER_BUTTON).click()

    @allure.step("Переход к карточке заказа")
    def click_orders_card(self):
        self.find_element(MainPageLocators.CARDS_LOCATOR).click()

    @allure.step("Переход по кнопке 'Оформить заказ'")
    def click_orders_register(self):
        self.find_element(MainPageLocators.BUTTON_ORDER_REGISTER).click()

    @allure.step("Получение номера заказа")
    def get_all_orders_count(self):
        return self.find_element(MainPageLocators.ID_ORDER).get_property("textContent")

    @allure.step("Закрытие карточки заказа")
    def close_card_click(self):
        self.find_element(MainPageLocators.CARD_CLOSE).click()

    @allure.step("Получение класса вкладки Конструктор")
    def get_selected_class_designer(self):
        return self.find_element(MainPageLocators.DESIGNER_BUTTON).get_attribute('class')

    @allure.step("Получение класса вкладки Лента заказов")
    def get_selected_class_order(self):
        return self.find_element(MainPageLocators.ORDER_BUTTON).get_attribute('class')

    @allure.step("Получение класса вкладки Лента заказов")
    def get_selected_class_ingredient(self):
        return self.find_element(MainPageLocators.CARD_INGREDIENT).get_attribute('class')

    @allure.step("Получение количества")
    def get_count_ingredient(self):
        return self.find_element(MainPageLocators.INGREDIENT_COUNT).get_property("textContent")

    @allure.step("Ожидание отображения кнопки Войти в аккаунт'")
    def wait_button_enter_account_visible(self):
        self.wait_element_visible(MainPageLocators.BUTTON_ENTER_ACCOUNT)

    @allure.step("Добавляем ингредиенты в заказ")
    def add_ingredient_in_order(self):
        self.drag_and_drop(MainPageLocators.CARDS_LOCATOR, MainPageLocators.ORDER_ADD)

    @allure.step("Ожидание отображения кнопки Оформить заказ")
    def wait_button_add_order_visible(self):
        self.wait_element_visible(MainPageLocators.BUTTON_ORDER_REGISTER)

    @allure.step("Ожидание отображения нового счетчика заказа'")
    def wait_num_order(self):
        self.wait_text_to_be_visible(MainPageLocators.INGREDIENT_COUNT, '0')

    @allure.step("Ожидание отображения номера заказа'")
    def wait_all_num_order(self):
        self.wait_text_to_be_visible(MainPageLocators.ORDER_ID, '9999')
