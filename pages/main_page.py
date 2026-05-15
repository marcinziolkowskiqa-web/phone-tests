from pages.base_page import BasePage


class MainPage(BasePage):
    def open_views(self) -> None:
        self.click_accessibility_id("Views")