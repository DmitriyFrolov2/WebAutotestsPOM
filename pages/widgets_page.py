import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select


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

        section_title = self.element_element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_element_is_visible(accordian[accordian_num]['content']).text
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
        color = self.element_element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        data = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_data_before = input_date.get_attribute('value')
        input_date.click()
        self.select_option_by_text(self.locators.DATE_SELECT_MONTH, data.month)
        self.select_option_by_text(self.locators.DATE_SELECT_YEAR, data.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, data.day)
        value_data_after = input_date.get_attribute('value')
        return value_data_before, value_data_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date_time = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_time_before = input_date_time.get_attribute("value")
        input_date_time.click()
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, "2020")
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_time_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_time_after = input_date_time_after.get_attribute("value")
        return value_date_time_before, value_date_time_after

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')

        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar.click()
        time.sleep(random.randint(2, 5))
        progress_bar.click()

        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                     'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT},
                }

        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(what_content)


class ToolsTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tooltip(self, hover_element, tool_tip_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(tool_tip_element)
        tool_tip = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        tool_tip_text = tool_tip.text
        return tool_tip_text

    def check_tooltips(self):
        tool_tip_text_button = self.get_text_from_tooltip(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        time.sleep(0.3)
        tool_tip_text_field = self.get_text_from_tooltip(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        time.sleep(0.3)
        tool_tip_text_contrary = self.get_text_from_tooltip(self.locators.CONTRARY_LINK,
                                                            self.locators.TOOL_TIP_CONTRARY)
        time.sleep(0.3)
        tool_tip_text_sections = self.get_text_from_tooltip(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        time.sleep(0.3)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_sections


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_lst = self.elements_are_present(self.locators.MENU_ITEMS_LIST)
        data = []
        for item in menu_item_lst:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def check_select_value(self):
        single_select_values = [
            "Group 1, option 1",
            "Group 1, option 2",
            "Group 2, option 1",
            "Group 2, option 2",
            "A root option",
            "Another root option"
        ]
        random_value = single_select_values[random.randint(0, 5)]
        single_select = self.element_is_visible(self.locators.SELECT_VALUE_DROPDOWN)
        single_select.send_keys(random_value)
        single_select.send_keys(Keys.RETURN)
        current_value = self.element_is_present(self.locators.SELECT_VALUE_DROPDOWN_RESULT).text
        return random_value, current_value

    def check_select_one_value(self):
        SELECT_ONE_VALUES = [
            {"label": "Dr.", "value": "dr"},
            {"label": "Mr.", "value": "mr"},
            {"label": "Mrs.", "value": "mrs"},
            {"label": "Ms.", "value": "ms"},
            {"label": "Prof.", "value": "prof"},
            {"label": "Other", "value": "other"}
        ]

        random_item = random.choice(SELECT_ONE_VALUES)
        input_text = random_item[random.choice(["label", "value"])]
        expected_text = random_item["label"]

        dropdown_element = self.element_is_visible(self.locators.SELECT_ONE_DROPDOWN)
        dropdown_element.send_keys(input_text)
        dropdown_element.send_keys(Keys.RETURN)

        selected_value = self.element_is_present(self.locators.SELECT_ONE_DROPDOWN_RESULT).text
        return expected_text, selected_value

    def check_old_style_select(self):
        dropdown = Select(self.element_is_visible(self.locators.OLD_SELECT))
        available_colors = next(generated_color()).color_name
        random_color = random.choice(available_colors)

        dropdown.select_by_visible_text(random_color)
        selected_text = dropdown.first_selected_option.text

        return selected_text, random_color

    def check_multi_select(self):
        MULTI_LIST = ["Green", "Blue", "Red", "Black"]

        random_values = random.sample(MULTI_LIST, k=random.randint(1, len(MULTI_LIST)))

        dropdown = self.element_is_visible(self.locators.MULTISELECT_DROPDOWN)

        for value in random_values:
            dropdown.send_keys(value)
            dropdown.send_keys(Keys.RETURN)
            time.sleep(0.3)

        selected_elements = self.elements_are_visible(self.locators.MULTISELECT_DROPDOWN_RESULTS)
        current_values = [el.text for el in selected_elements]

        return random_values, current_values

    def are_multiselected_items_removed(self):
        remove_buttons = self.element_is_visible(self.locators.ALL_REMOVE_BUTTON)
        remove_buttons.click()
        is_removed = self.element_is_not_visible(self.locators.MULTISELECT_DROPDOWN_RESULTS)
        return is_removed

    def check_standart_multiselect(self):
        standard_select_element = self.element_is_visible(self.locators.STANDART_SELECT)
        self.go_to_element(standard_select_element)
        select = Select(standard_select_element)

        options_to_select = ["Volvo", "Saab", "Opel", "Audi"]

        for option_text in options_to_select:
            select.select_by_visible_text(option_text)

        selected_options_elements = select.all_selected_options

        actual_selected_texts = [option_element.text for option_element in selected_options_elements]

        return options_to_select, actual_selected_texts
