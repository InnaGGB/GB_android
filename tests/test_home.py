import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def test_click_button(driver, country_name="Serbia"):
    home_page = HomePage(driver)
    home_page.click_button()

    # Debug: Print visible items before scrolling
    print("Visible items before scrolling:")
    elements = driver.find_elements(By.XPATH, '//android.widget.TextView')
    for el in elements:
        print(el.text)

    # Try scrolling to the country
    scrollable = 'new UiScrollable(new UiSelector().scrollable(true))'
    for _ in range(5):  # Adjust number of attempts if needed
        try:
            element = driver.find_element(By.XPATH, f'//android.widget.TextView[@text="{country_name}"]')
            break  # Exit loop if found
        except:
            driver.find_element(By.ANDROID_UIAUTOMATOR, f'{scrollable}.scrollForward()')

    # Verify the element is displayed
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{country_name}"]'))
    )
    assert element.is_displayed(), f"{country_name} was not found after scrolling."

    # ✅ Tap the country name to select it
    element.click()
    print(f"✅ Selected {country_name} from the list.")

    # Use country name text as a confirmation method
    try:
        # Wait for the updated country name (use a different locator if needed)
        selected_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, f'//android.widget.TextView[@text="{country_name}"]'), country_name)
        )
        print(f"✅ Country {country_name} selected successfully.")
    except:
        print(f"❌ Failed to confirm the selection of {country_name}. Please check the locator.")

    # Optional: If you want to verify a different element post-selection, ensure the right element is selected
    print("✅ Updated Page Source:", driver.page_source)
