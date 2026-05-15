import pytest
from pages.main_page import MainPage
from pages.views_page import ViewsPage
from pages.controls_page import ControlsPage


@pytest.mark.parametrize(
    "input_text",
    [
        "Marcin testuje Appium",
        "Hello Appium",
        "123456",
        "test_!@#",
    ],
    ids=[
        "long_text",
        "simple_text",
        "digits_only",
        "special_chars",
    ]
)
def test_dark_theme_form_data_driven(driver, input_text):
    main_page = MainPage(driver)
    views_page = ViewsPage(driver)
    controls_page = ControlsPage(driver)

    main_page.open_views()
    views_page.open_controls()
    controls_page.open_dark_theme()

    controls_page.enter_text(input_text)

    assert controls_page.get_text() == input_text