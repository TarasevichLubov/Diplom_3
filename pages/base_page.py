import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу")
    def go_to_page(self, url):
        return self.driver.get(url)

    def find_element(self, locator, wait_time=20):
        return WebDriverWait(self.driver, wait_time)\
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"Невозможно отобразить элемент с локатором = {locator}")

    def find_elements(self, locator, wait_time=20):
        return WebDriverWait(self.driver, wait_time)\
            .until(expected_conditions.presence_of_all_elements_located(locator),
                   message=f"Невозможно отобразить элементы с локатором = {locator}")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.element_to_be_clickable(element),
                   message=f"Невозможно отобразить элемент")

    def change_window(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])

    def current_url(self):
        return self.driver.current_url
