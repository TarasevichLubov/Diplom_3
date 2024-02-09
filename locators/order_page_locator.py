from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_CARD = (By.XPATH, ".//div[contains(@class, 'OrderFeed_contentBox')]/ul/li[1]")
    ALL_ORDERS = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    DAY_ORDERS = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_READY = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[1]")
    CARD_VIEW = (By.XPATH, ".//section[2][contains(@class, 'Modal_modal__P3_V5')]")
    HISTORY_ORDER = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    ORDER_CARDS_LOCATOR = (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")
