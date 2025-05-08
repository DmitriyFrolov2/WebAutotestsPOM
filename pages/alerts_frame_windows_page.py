import time
import random

import allure

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    @allure.step('check opened new tab ')
    def check_opened_new_tub(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.go_to_new_window(1)
        title_text =self. get_element_text(self.locators.TITLE_NEW_TAB)
        return title_text

    @allure.step('check opened new window')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.go_to_new_window(1)
        title_text =self. get_element_text(self.locators.TITLE_NEW_TAB)
        return title_text


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    @allure.step('get text from alert')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.go_to_alert()
        return alert_window.text


    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.go_to_alert()
        return alert_window.text

    @allure.step('check alert appear after 5 sec')
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.go_to_alert()
        alert_window.accept()
        text_result = self. get_element_text(self.locators.CONFIRM_ALERT_RESULT)
        return text_result

    @allure.step('check dismiss alert')
    def check_dismiss_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.go_to_alert()
        alert_window.dismiss()
        text_result = self. get_element_text(self.locators.CONFIRM_ALERT_RESULT)
        return text_result

    @allure.step('check prompt alert')
    def check_prompt_alert(self):
        text = f'autotest{random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.go_to_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self. get_element_text(self.locators.PROMPT_ALERT_RESULT)
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('check frame1')
    def check_frame1(self,frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.go_to_frame(frame)
            text = self. get_element_text(self.locators.TITLE_FRAME)
            self.driver.switch_to.default_content()
            return [width, height, text]

    @allure.step('check frame2')
    def check_frame2(self,frame_num):
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.go_to_frame(frame)
            text =  self.get_element_text(self.locators.TITLE_FRAME)
            self.driver.switch_to.default_content()
            return [width, height, text]



class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.go_to_frame(parent_frame)
        parent_text =  self.get_element_text(self.locators.PARENT_TEXT)
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.go_to_frame(child_frame)
        child_text =  self.get_element_text(self.locators.CHILD_TEXT)
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('check small modal dialogs')
    def check_small_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title = self.get_element_text(self.locators.TITLE_SMALL_MODAL)
        text = self.get_element_text(self.locators.TEXT_SMALL_MODAL)
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL_BUTTON).click()
        return title, text

    @allure.step('check large modal dialogs')
    def check_large_modal_dialogs(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title = self.get_element_text(self.locators.TITLE_LARGE_MODAL)
        text = self.get_element_text(self.locators.TEXT_LARGE_MODAL)
        self.element_is_visible(self.locators.CLOSE_LARGE_MODAL_BUTTON).click()
        return title, text
