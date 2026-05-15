import os
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver(request):

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    options.device_name = "10HF4SFJJ6000BZ"
    options.udid = "10HF4SFJJ6000BZ"

    options.app_package = "io.appium.android.apis"
    options.app_activity = ".ApiDemos"

    options.no_reset = False

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    # dostęp do drivera w hookach pytest
    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"

            try:
                driver.save_screenshot(screenshot_path)
                print(f"\nScreenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"\nCould not save screenshot: {e}")