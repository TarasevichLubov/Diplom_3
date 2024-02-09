from selenium.webdriver.common.by import By


class AccountPageLocators:

    HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
    HISTORY_CARD = (By.XPATH, ".//p[@class='text text_type_digits-default']")
