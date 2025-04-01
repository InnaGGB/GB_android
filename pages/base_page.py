from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Waits for an element to be present and returns it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Finds an element and clicks it."""
        self.find_element(locator).click()

