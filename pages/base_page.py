from pathlib import Path
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_accessibility_id(self, value: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, value))
        ).click()

    def click_id(self, value: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, value))
        ).click()

    def type_id(self, value: str, text: str, clear: bool = True) -> None:
        element = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, value))
        )
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text_by_id(self, value: str) -> str:
        element = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, value))
        )
        return element.text

    def get_attribute_by_id(self, value: str, attr: str) -> str:
        element = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, value))
        )
        return element.get_attribute(attr)

    def save_screenshot(self, file_path: str) -> None:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        self.driver.save_screenshot(file_path)