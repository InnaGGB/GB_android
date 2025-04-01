import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")
def driver():
    """Set up Appium driver."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "670d21c8"  # Replace with your device ID
    options.app_package = "com.glambook.master"
    options.app_activity = "com.glambook.master.MainActivity"
    options.automation_name = "UiAutomator2"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_click_button(driver, country_name="United States"):
    home_page = HomePage(driver)
    home_page.click_button()
    # Scroll until the country code with the exact XPath is visible
    element = driver.find_element_by_xpath(f'//android.widget.TextView[@text="{country_name}"]')

    # Wait for the element to appear, if necessary
    time.sleep(2)  # or WebDriverWait if you want to wait explicitly

    # If the element is not yet visible, scroll until it's found
    if not element.is_displayed():
        # Perform scrolling using TouchAction or UiScrollable if needed
        action = TouchAction(driver)
        action.press(x=300, y=1000).move_to(x=300, y=300).release().perform()  # Adjust coordinates for scrolling

        # Wait for the list to reload
        time.sleep(2)

        # Find the element again after scroll
        element = driver.find_element_by_xpath(f'//android.widget.TextView[@text="{country_name}"]')

    # Verify that the element is visible now
    print(f"Scrolled to {country_name}.")

    # Force Appium to refresh by printing the new UI structure
    print("Updated Page Source:", driver.page_source)









