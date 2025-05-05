import os
import random
import time
import base64
import re
import allure

import requests

from generator.generator import generated_person, generate_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1].strip()
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1].strip()
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1].strip()
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1].strip()
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.CHECK_BOXES_ITEM_LIST)
        count = 10
        while count != 0:
            item = item_list[random.randint(1, 5)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("Clicking on each button")
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = random.randint(1, 3)
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_clickable(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step("Get number of rows")
    def get_rows_count(self):
        table_rows = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        return len(table_rows)

    @allure.step("Select from rows dropdown")
    def select_from_rows_dropdown(self):
        rows_numbers = [5, 10, 20]
        data = []
        for number in rows_numbers:
            rows_dropdown = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(rows_dropdown)
            rows_dropdown.click()
            time.sleep(0.2)
            Select(rows_dropdown).select_by_value(str(number))
            data.append(self.get_rows_count())
        return data


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def perform_double_click_button(self):
        double_click_button = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        self.action_double_click(double_click_button)
        return self.get_double_click_message()

    def perform_right_click_button(self):
        right_click_button = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
        self.action_right_click(right_click_button)
        return self.get_right_click_message()

    def perform_click_button(self):
        if self.element_is_visible(self.locators.CLICK_ME_BUTTON).is_displayed():
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.get_click_message()
        else:
            return False

    def get_double_click_message(self):
        return self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE).text

    def get_right_click_message(self):
        return self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE).text

    def get_click_message(self):
        return self.element_is_visible(self.locators.CLICK_MESSAGE).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    API_CALL_URLS = [
        'created',
        'no-content',
        'moved',
        'bad-request',
        'unauthorized',
        'forbidden',
        'invalid-url'
    ]

    @allure.step("Getting response from home link")
    def check_home_link(self):
        home_link = self.element_is_visible(self.locators.HOME_LINK)
        home_link_href = home_link.get_attribute("href")
        response = requests.get(home_link_href)

        if response.status_code == 200:
            home_link.click()
            time.sleep(2)
            self.switch_tab_by_handle(1)
            current_url = self.driver.current_url
            return home_link_href, current_url  # Кортеж из двух строк
        else:
            return f'Invalid status code. Response status code: {response.status_code}. Link href: {home_link_href}'

    @allure.step("Getting responses from links")
    def check_api_call_links(self):
        api_call_locators = self.locators.API_CALL_LINKS
        api_call_links = [self.element_is_visible(link_locator) for link_locator in api_call_locators]
        status_codes = []
        messages = []
        for api_call_link in api_call_links:
            self.go_to_element(api_call_link)
            api_call_link.click()
            time.sleep(1)
            response_text = self.element_is_present(self.locators.LINK_RESPONSE, ).text
            response_statuscode = re.search(r'\d+', response_text).group()
            message = response_text[50:].lower()

            status_codes.append(response_statuscode)
            messages.append(message)
        return status_codes, messages

    @allure.step("Getting response codes from links")
    def send_calls_get_status_code(self):
        api_call_urls = [f'https://demoqa.com/{link}' for link in self.API_CALL_URLS]
        response_codes = []
        for url in api_call_urls:
            response = requests.get(url)
            response_codes.append(str(response.status_code))
        return response_codes

    @allure.step("Getting text of links")
    def get_api_call_links_text(self) -> list[str]:
        api_call_locators = self.locators.API_CALL_LINKS
        api_call_links = [self.element_is_visible(link_locator) for link_locator in api_call_locators]
        api_call_links_text = self.get_text_from_webelements(api_call_links)
        return api_call_links_text


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    @allure.step("Uploading generated file")
    def upload_file(self):

        file_name = generate_file()
        downloads_dir = os.path.join(os.getcwd(), "downloads")
        path = os.path.join(downloads_dir, file_name)

        try:
            self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
            return file_name
        finally:
            if os.path.exists(path):
                os.remove(path)

    @allure.step("Getting uploaded file name from page")
    def get_uploaded_file_name(self):

        uploaded_text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return os.path.basename(uploaded_text)

    @allure.step("Downloading test file")
    def download_file(self):

        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)

        # Создаем путь к файлу в папке downloads
        file_name = f"filetest{random.randint(0, 999)}.jpg"
        path = os.path.join(os.getcwd(), "downloads", file_name)

        # Сохраняем файл
        with open(path, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path)

        os.remove(path)

        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step("Checking if button becomes enabled")
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step("Checking button color change")
    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step("Checking if button appears after delay")
    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True
