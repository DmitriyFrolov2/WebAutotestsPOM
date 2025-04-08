import os
import random
import time
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from generator.generator import generated_person, generate_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


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

    def select_up_to_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.check_count_rows())
            return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(
            self.locators.FULL_PERSON_LIST)
        return len(list_rows)


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

    def check_simple_link_opens_new_tab(self, wait_timeout=10):  # Добавим параметр таймаута ожидания
        """
        Находит 'Home' ссылку, проверяет ее статус-код,
        если 200, открывает в новой вкладке с помощью JS,
        переключается на нее, ЖДЕТ ЗАГРУЗКИ URL и возвращает
        исходный href и URL новой вкладки.
        Возвращает (href, status_code) если статус не 200.
        """
        simple_link_element = self.element_is_visible(self.locators.SIMPLE_LINK)
        if not simple_link_element:
            print("Не найдена 'Home' ссылка (SIMPLE_LINK)")
            return None, "Element Not Found"

        link_href = simple_link_element.get_attribute('href')
        if not link_href:
            print("У 'Home' ссылки нет атрибута href")
            return None, "Href Not Found"

        # --- Проверка статуса ---
        # Убедимся, что href валиден для запроса
        if not link_href.startswith('http'):
            print(f"Href '{link_href}' не является URL, статус не проверяется.")

            status_code = 200
        else:
            status_code = self.get_status_code(link_href)

        # --- Логика открытия вкладки ---
        if status_code == 200:
            print(
                f"Ссылка '{link_href}' (или элемент без URL) считается готовой к открытию. Открываем в новой вкладке.")
            initial_window_count = len(self.driver.window_handles)  # Запоминаем количество окон

            # Открываем вручную через JS
            self.execute_script(f"window.open('{link_href}', '_blank');")

            # --- Ожидание новой вкладки ---
            try:
                print("Ожидание открытия новой вкладки...")
                WebDriverWait(self.driver, wait_timeout).until(
                    EC.number_of_windows_to_be(initial_window_count + 1)
                )
                print("Новая вкладка обнаружена.")
            except TimeoutException:
                print(f"Новая вкладка не открылась за {wait_timeout} секунд.")
                return link_href, "New Tab Did Not Open"

            # --- Переключение на новую вкладку ---
            self.switch_to_new_tab()  # Используем метод из BasePage

            # --- ОЖИДАНИЕ ЗАГРУЗКИ URL (КЛЮЧЕВОЕ ИЗМЕНЕНИЕ) ---
            try:
                print(f"Ожидание изменения URL с 'about:blank' в новой вкладке (макс. {wait_timeout} сек)...")
                # Ждем, пока URL перестанет быть 'about:blank' ИЛИ станет равен link_href
                # Лямбда - это как сокращенная запись для простой функции, которая сразу возвращает результат одного вычисления
                WebDriverWait(self.driver, wait_timeout).until(
                    lambda driver: driver.current_url != 'about:blank' and driver.current_url.startswith('http')

                )
                current_url = self.get_current_url()
                print(f"URL в новой вкладке загружен: {current_url}")

                # Дополнительная проверка на всякий случай
                if current_url == 'about:blank':
                    print("!!! Ошибка: URL остался 'about:blank' после ожидания.")
                    return link_href, "URL Did Not Load Properly"

                return link_href, current_url  # возвращаем href и загруженный URL

            except TimeoutException:
                final_url = self.get_current_url()  # Получаем URL, который есть на момент таймаута
                print(
                    f"Тайм-аут ({wait_timeout} сек) ожидания загрузки URL в новой вкладке. Финальный URL: {final_url}")
                # Возвращаем то, что есть, чтобы тест показал реальный результат
                return link_href, final_url

        else:
            # Если статус был не 200 (и это был валидный URL)
            print(f"Ссылка '{link_href}' вернула статус {status_code}. Новая вкладка не открывалась.")
            return link_href, status_code  # Возвращаем href и статус-код ошибки

    def get_link_status_via_request(self, locator):
        """
        Находит элемент по локатору, получает его href
        и возвращает статус-код, полученный через requests.
        """
        link_element = self.element_is_present(locator)  # Используем present, т.к. элемент может быть не видим
        if not link_element:
            print(f"Не найден элемент по локатору: {locator}")
            return None

        link_href = link_element.get_attribute('href')
        if not link_href:
            print(f"У элемента {locator} нет атрибута href")
            return None

        print(f"Проверяем статус для URL: {link_href}")
        status_code = self.get_status_code(link_href)
        return status_code

    def click_api_link_and_get_response_text(self, locator):
        """
        Кликает по ссылке, которая должна вызвать API-запрос (без навигации),
        ожидает появления ответа на странице и возвращает текст ответа.
        """
        link_element = self.element_is_visible(locator)
        if not link_element:
            print(f"Не найден кликабельный элемент по локатору: {locator}")
            return None

        # Запоминаем текущий текст ответа, чтобы дождаться его изменения
        initial_response_text = self.get_element_text(self.locators.LINK_RESPONSE)

        link_element.click()

        # Ждем, пока текст в блоке ответа изменится или появится

        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.get_element_text(self.locators.LINK_RESPONSE) != initial_response_text and \
                               self.get_element_text(self.locators.LINK_RESPONSE) is not None
            )
        except TimeoutException:
            print("Текст ответа не появился или не изменился после клика.")
            # Возвращаем текущий текст, даже если он не изменился
            return self.get_element_text(self.locators.LINK_RESPONSE)

        response_text = self.get_element_text(self.locators.LINK_RESPONSE)
        print(f"Получен ответ после клика по {locator}: '{response_text}'")
        return response_text


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        """Загружает файл и возвращает его имя"""
        file_name = generate_file()
        path = os.path.join(os.getcwd(), "downloads", file_name)
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        return file_name

    def get_uploaded_file_name(self):
        uploaded_text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return os.path.basename(uploaded_text)

    def download_file(self):
        """Скачивает файл и проверяет его наличие"""
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


    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True



    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after


    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True




