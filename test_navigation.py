from pages.main_page import MainPage
from pages.views_page import ViewsPage

def test_views_controls_navigation(driver):
    main_page = MainPage(driver)
    views_page = ViewsPage(driver)

    main_page.open_views()
    views_page.open_controls()