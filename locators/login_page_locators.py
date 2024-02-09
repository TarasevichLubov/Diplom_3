from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_ACCOUNT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASS_ACCOUNT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")
