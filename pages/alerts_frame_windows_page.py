import time
import random
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators
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


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.check_alert_message()
        return alert_window.text


    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.check_alert_message()
        return alert_window.text


    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.check_alert_message()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_ALERT_RESULT).text
        return text_result


    def check_dismiss_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.check_alert_message()
        alert_window.dismiss()
        text_result = self.element_is_present(self.locators.CONFIRM_ALERT_RESULT).text
        return text_result


    def check_prompt_alert(self):
        text = f'autotest{random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.check_alert_message()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_ALERT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame1(self,frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [width, height, text]


    def check_frame2(self,frame_num):
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [width, height, text]






