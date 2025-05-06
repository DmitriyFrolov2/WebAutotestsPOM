from conftest import PICTURE_PATH
from selenium.webdriver import Keys
from generator.generator import generated_person, generate_subject
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage
import random
import time
import allure

class FormPage(BasePage):
    locators = FormPageLocators()

    @allure.step("Заполняем форму")
    def fill_form_fields(self):
        person = next(generated_person())
        subject_form = generate_subject()
        self._fill_basic_info(person)
        self._select_subject(subject_form)
        self._select_hobby()
        self._upload_file(str(PICTURE_PATH))
        self._fill_address(person)
        self._submit_form()
        return person

    @allure.step("Заполняем основную информацию")
    def _fill_basic_info(self, person):
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_MALE).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)

    @allure.step("Выбираем предмет")
    def _select_subject(self, subject):
        self.element_is_visible(self.locators.SUBJECT).send_keys(subject)
        time.sleep(1)
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        time.sleep(0.2)

    @allure.step("Выбираем хобби")
    def _select_hobby(self):
        hobby_locators = [
            self.locators.HOBBY_SPORT,
            self.locators.HOBBY_READING,
            self.locators.HOBBY_MUSIC
        ]
        random_chosen_locator = random.choice(hobby_locators)
        self.js_click_element(random_chosen_locator)
        time.sleep(1)

    @allure.step("Загружаем файл")
    def _upload_file(self, file_path):
        self.element_is_present(self.locators.FILE_INPUT).send_keys(file_path)

    @allure.step("Заполняем адрес и выбираем регион")
    def _fill_address(self, person):
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.click_element(self.locators.SELECT_STATE)
        time.sleep(1)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        time.sleep(1)
        self.click_element(self.locators.SELECT_CITY)
        time.sleep(1)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        time.sleep(1)

    @allure.step("Отправляем форму")
    def _submit_form(self):
        self.click_element(self.locators.SUBMIT)

    @allure.step("Получаем результат из таблицы")
    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data