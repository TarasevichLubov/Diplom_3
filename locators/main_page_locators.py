from selenium.webdriver.common.by import By


class MainPageLocators:

    ACCOUNT = (By.XPATH, ".//a[@href='/account']")
    EMAIL_ACCOUNT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASS_ACCOUNT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    DESIGNER_BUTTON = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    ORDER_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    CARDS_LOCATOR = (By.XPATH, ".//img[@alt='Краторная булка N-200i']/parent::a")
    BUTTON_ORDER_REGISTER = (By.XPATH, ".//button[text()='Оформить заказ']")
    CARD_INGREDIENT = (By.XPATH, ".//section[1][contains(@class, 'Modal_modal')]")
    ORDER_ID = (By.XPATH, ".//p[text()='идентификатор заказа']/preceding-sibling::h2")
    CARD_CLOSE = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    ORDER_ADD = (By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket__list')]")
    INGREDIENT_COUNT = (By.XPATH, ".//img[@alt='Краторная булка N-200i']/preceding-sibling::div/p")
    ID_ORDER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq)']")
    HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    HISTORY_CARD = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
