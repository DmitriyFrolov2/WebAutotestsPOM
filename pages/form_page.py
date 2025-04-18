import os
from selenium.webdriver import Keys
from generator.generator import generated_person, generate_subject, generate_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, file_path = generate_file()
        subject_form = generate_subject()

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys(subject_form)
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(file_path)
        os.remove(file_path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.click_element(self.locators.SELECT_STATE)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.click_element(self.locators.SELECT_CITY)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.click_element(self.locators.SUBMIT)
        return person

    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
