import os
import pytest
import allure

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
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    # screenshot tylko przy failu testu
    if report.when == "call" and report.failed:

        driver = getattr(item, "driver", None)

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                f"screenshots/{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)

            # attach do Allure
            with open(screenshot_path, "rb") as image_file:

                allure.attach(
                    image_file.read(),
                    name=item.name,
                    attachment_type=allure.attachment_type.PNG
                )

            print(f"\nScreenshot saved: {screenshot_path}")