from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()
    def check_opened_new_tub(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_new_tab()
        title_text =self.element_is_present(self.locators.TITLE_NEW_TAB).text
        return title_text



    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_new_tab()
        title_text =self.element_is_present(self.locators.TITLE_NEW_TAB).text
        return title_text
