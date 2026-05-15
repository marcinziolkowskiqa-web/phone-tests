from pages.main_page import MainPage
from pages.views_page import ViewsPage
from pages.controls_page import ControlsPage


def test_dark_theme_form(driver):
    main_page = MainPage(driver)
    views_page = ViewsPage(driver)
    controls_page = ControlsPage(driver)

    main_page.open_views()
    views_page.open_controls()
    controls_page.open_dark_theme()

    controls_page.enter_text("Marcin testuje Appium")
    controls_page.check_checkbox()

    assert controls_page.get_text() == "Marcin testuje Appium"
    assert controls_page.is_checkbox_checked() is True