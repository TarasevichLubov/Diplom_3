from selenium.webdriver.common.by import By


class ResetPassPageLocators:
    VISIBLE_PASS = (By.CLASS_NAME, "input__icon.input__icon-action")
    VIEW_PASSWORD = (By.XPATH, ".//label[text()='Пароль']")