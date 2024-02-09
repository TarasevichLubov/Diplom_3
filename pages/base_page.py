import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу.")
    def go_to_page(self, url):
        return self.driver.get(url)

    @allure.step("Найти элемент на странице.")
    def find_element(self, locator, wait_time=20):
        return WebDriverWait(self.driver, wait_time)\
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"Невозможно отобразить элемент с локатором = {locator}")

    @allure.step("Найти элементы на странице.")
    def find_elements(self, locator, wait_time=20):
        return WebDriverWait(self.driver, wait_time)\
            .until(expected_conditions.presence_of_all_elements_located(locator),
                   message=f"Невозможно отобразить элементы с локатором = {locator}")

    @allure.step("Перейти к элементу на странице.")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.element_to_be_clickable(element),
                   message=f"Невозможно отобразить элемент")

    @allure.step("Перейти к другому окну.")
    def change_window(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])

    @allure.step("Вывести текущий адрес страницы.")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Перенести элемент.")
    def drag_and_drop(self, locator_1, locator_2):
        element = self.driver.find_element(*locator_1)
        target = self.driver.find_element(*locator_2)
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element, target).perform()

    @allure.step("Нажать клавишу.")
    def send_keys(self, locator, value, wait_time=20):
        element = WebDriverWait(self.driver, wait_time) \
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"Невозможно отобразить элемент с локатором = {locator}")
        element.send_keys(value)

    @allure.step("Получаем список текстовых значений элементов.")
    def get_list_element(self, list_element):
        list_elem = []
        for element in list_element:
            list_elem.append(element.text)
        return list_elem

    @allure.step("Ожидание отображения элемента.")
    def wait_element_visible(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((locator)))

    @allure.step("Ожидание исчезновения текста.")
    def wait_text_to_be_visible(self, locator, value):
        wait = WebDriverWait(self.driver, 20)
        wait.until_not(expected_conditions.text_to_be_present_in_element(locator, value))

    @allure.step("Ожидание проверки пропажи элемента.")
    def wait_element_invisible(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.invisibility_of_element(locator))
