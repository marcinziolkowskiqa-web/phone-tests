from pages.base_page import BasePage


class ViewsPage(BasePage):
    def open_controls(self) -> None:
        self.click_accessibility_id("Controls")