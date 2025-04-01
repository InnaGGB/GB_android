from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SET_UP_YOUR_BUSINESS_BUTTON_LOCATOR = (By.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.Button")
    COUNTRY_CODE_LIST_BUTTON_LOCATOR = (By.XPATH, "//android.widget.ScrollView/android.widget.Button")

    def click_button(self):
        """Clicks the button on the home screen."""
        self.click_element(self.SET_UP_YOUR_BUSINESS_BUTTON_LOCATOR)
        self.click_element(self.COUNTRY_CODE_LIST_BUTTON_LOCATOR)

