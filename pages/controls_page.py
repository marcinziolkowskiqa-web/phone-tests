from pages.base_page import BasePage


class ControlsPage(BasePage):
    EDIT_ID = "io.appium.android.apis:id/edit"
    CHECKBOX_ID = "io.appium.android.apis:id/check1"

    def open_dark_theme(self) -> None:
        self.click_accessibility_id("2. Dark Theme")

    def enter_text(self, text: str) -> None:
        self.type_id(self.EDIT_ID, text)

    def get_text(self) -> str:
        return self.get_text_by_id(self.EDIT_ID)

    def check_checkbox(self) -> None:
        self.click_id(self.CHECKBOX_ID)

    def is_checkbox_checked(self) -> bool:
        return self.get_attribute_by_id(self.CHECKBOX_ID, "checked") == "true"