from selenium.webdriver.common.by import By


class ForgotPageLocators:

    RECOVER_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")
    RECOVER_PASSWORD_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    EMAIL_RECOVER = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
