import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutocompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.MULTI_INPUT)
            )
            input_multi.click()
            input_multi.send_keys(color)
            time.sleep(0.2)
            input_multi.send_keys(Keys.RETURN)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def clear_all_from_multi(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.CLEAR_ALL_BUTTON)
        ).click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.locators.CLEAR_ALL_BUTTON)
            )
            return True
        except TimeoutException:
            return False


    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        time.sleep(0.2)
        input_single.send_keys(Keys.RETURN)
        return color[0]


    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text