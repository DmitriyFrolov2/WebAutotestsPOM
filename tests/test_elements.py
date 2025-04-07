import pytest

from locators.elements_page_locators import LinksPageLocators
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage
import random
import re


class TestTextBox:

    @pytest.mark.usefixtures("chrome_only")
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
        # Проверяем, что введённые данные совпадает с отображённым на странице
        assert full_name == output_name, f"Expected: {full_name}, Actual: {output_name}"
        assert email == output_email, f"Expected: {email}, Actual: {output_email}"
        assert current_address == output_cur_addr, f"Expected: {current_address}, Actual: {output_cur_addr}"
        assert permanent_address == output_per_addr, f"Expected: {permanent_address}, Actual: {output_per_addr}"


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, 'чекбоксы не были выбраны'


class TestRadioButton:
    @pytest.mark.usefixtures("chrome_only")
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', "Ожидалось, что будет выбран вариант 'Yes'."
        assert output_impressive == 'Impressive', "Ожидалось, что будет выбран вариант 'Impressive'."
        assert output_no == "No", "Ожидалось, что будет выбран вариант 'No'."


class TestWebTables:
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, 'Такого человека нет в таблице'

    @pytest.mark.usefixtures("chrome_only")
    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, "Возраст не был обновлён"

    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted_person()
        assert text == 'No rows found', 'человек не был удалён'

    def test_web_table_change_count_rows(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_up_to_rows()
        assert count == [5, 10, 20, 25, 50, 100], "Количество строк в таблице не изменилось или изменилось некорректно."


class TestButtonsPage:
    def test_double_click_button(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        actual_message = button_page.perform_double_click_button()
        expected_message = "You have done a double click"
        assert actual_message == expected_message, f"Ожидалось сообщение после двойного клика: '{expected_message}', но получено: '{actual_message}'."

    def test_right_click_button(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        actual_message = button_page.perform_right_click_button()
        expected_message = "You have done a right click"
        assert actual_message == expected_message, f"Ожидалось сообщение после правого клика: '{expected_message}', но получено: '{actual_message}'."

    def test_click_me_button(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        actual_message = button_page.perform_click_button()
        expected_message = "You have done a dynamic click"
        assert actual_message == expected_message, f"Ожидалось сообщение после обычного клика: '{expected_message}', но получено: '{actual_message}'."


class TestLinksPage:

    @pytest.fixture(scope="function")
    def links_page(self, driver):

        page = LinksPage(driver, "https://demoqa.com/links")
        page.open()
        return page

    def test_simple_link_opens_new_tab(self, links_page):
        """
        Проверяет, что 'Home' ссылка открывается в новой вкладке
        и URL новой вкладки совпадает с href ссылки (если статус 200).
        """

        href_link, result = links_page.check_simple_link_opens_new_tab()

        assert href_link is not None, "Не удалось получить href 'Home' ссылки."

        # Проверяем, что если был возвращен URL, он совпадает с href
        if isinstance(result, str) and result.startswith("https"):
            assert result == href_link
        # Проверяем, что если был возвращен статус-код, он не 200
        elif isinstance(result, int):
            assert result != 200, \
                f"Статус ссылки был {result}, но ожидалось открытие новой вкладки (статус 200)."
            print(f"Информация: Ссылка имеет статус {result}, новая вкладка не открывалась, как и ожидалось.")
        else:
            pytest.fail(f"Неожиданный результат от check_simple_link_opens_new_tab: {result}")

    @pytest.mark.xfail(reason="Опечатка 'staus' вместо 'status' "
                              "препятствует корректному парсингу ответа.")
    @pytest.mark.parametrize(
        "link_locator, expected_status_code, link_name",
        [
            (LinksPageLocators.CREATED_LINK, 201, "Created"),
            (LinksPageLocators.NO_CONTENT_LINK, 204, "No Content"),
            (LinksPageLocators.MOVED_LINK, 301, "Moved Permanently"),
            (LinksPageLocators.BAD_REQUEST_LINK, 400, "Bad Request"),
            (LinksPageLocators.UNAUTHORIZED_LINK, 401, "Unauthorized"),
            (LinksPageLocators.FORBIDDEN_LINK, 403, "Forbidden"),
            (LinksPageLocators.NOT_FOUND_LINK, 404, "Not Found"),
        ]
    )
    def test_api_link_response(self, links_page, link_locator, expected_status_code, link_name):

        print(f"\nТест: Проверка API ссылки '{link_name}' (ожидается статус {expected_status_code})")
        response_text = links_page.click_api_link_and_get_response_text(link_locator)

        assert response_text is not None, f"Не получен текст ответа для ссылки '{link_name}'."

        # Пример строки: "Link has responded with status 201 and status text Created"
        match = re.search(r"status (\d{3}) and status text ([\w\s]+)", response_text)
        # match = re.search(r"(?:sta|sta\w+) (\d{3}) and status text ([\w\s]+)", response_text) - код для запуска теста без ошибки

        assert match, f"Не удалось извлечь статус из текста ответа: '{response_text}'"

        actual_status_code = int(match.group(1))
        actual_status_text = match.group(2)

        assert actual_status_code == expected_status_code, \
            f"Неверный статус-код в ответе для '{link_name}'. Ожидался: {expected_status_code}, Получен: {actual_status_code} (Текст: '{response_text}')"

        print(f"Успех: Клик по '{link_name}' вызвал ответ со статусом {actual_status_code} ({actual_status_text})")


class TestUploadAndDownloadPage:
    @pytest.mark.usefixtures("chrome_only")
    def test_upload_file(self, driver):
        upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_page.open()
        expected_name = upload_page.upload_file()
        actual_name = upload_page.get_uploaded_file_name()
        assert expected_name == actual_name, \
            f"Ожидалось: {expected_name}, загружено: {actual_name}"



    def test_download_file(self, driver):
        download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        download_page.open()
        check = download_page.download_file()
        assert check is True, "Файл не был скачан"
