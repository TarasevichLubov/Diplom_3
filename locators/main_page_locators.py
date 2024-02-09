from selenium.webdriver.common.by import By


class MainPageLocators:

    ACCOUNT = (By.XPATH, ".//a[@href='/account']")
    DESIGNER_BUTTON = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    ORDER_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    CARDS_LOCATOR = (By.XPATH, ".//img[@alt='Краторная булка N-200i']/parent::a")
    BUTTON_ORDER_REGISTER = (By.XPATH, ".//button[text()='Оформить заказ']")
    CARD_INGREDIENT = (By.XPATH, ".//section[1][contains(@class, 'Modal_modal')]")
    ORDER_ID = (By.XPATH, ".//div/h2[text()='9999']")
    CARD_CLOSE = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    ORDER_ADD = (By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket__list')]")
    INGREDIENT_COUNT = (By.XPATH, ".//img[@alt='Краторная булка N-200i']/preceding-sibling::div/p")
    ID_ORDER = (By.XPATH, ".//p[text()='идентификатор заказа']/preceding-sibling::h2")
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
    BUTTON_ENTER_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")
