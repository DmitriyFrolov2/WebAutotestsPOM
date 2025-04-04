import pytest
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage
import random


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

