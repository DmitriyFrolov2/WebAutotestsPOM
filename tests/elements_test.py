import allure
import pytest


from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage
import random


@allure.suite("Elements Page")
class TestElementsPage:
    @allure.feature("Text Box")
    class TestTextBox:
        @allure.title("Text Box test")
        # @pytest.mark.usefixtures("chrome_only")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, f"Expected: {full_name}, Actual: {output_name}"
            assert email == output_email, f"Expected: {email}, Actual: {output_email}"
            assert current_address == output_cur_addr, f"Expected: {current_address}, Actual: {output_cur_addr}"
            assert permanent_address == output_per_addr, f"Expected: {permanent_address}, Actual: {output_per_addr}"

    @allure.feature("Check Box")
    class TestCheckBox:
        @allure.title("Check Box test")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'чекбоксы не были выбраны'

    @allure.feature("Radio Button")
    class TestRadioButton:
        @allure.title("Radio Button test")
        @pytest.mark.xfail(reason="Тест падает из-за неактивной кнопки 'No'")
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

    @allure.feature("Web Table")
    class TestWebTables:
        @allure.title("Add new person to the table")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        @allure.title("Search person in the table")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'Такого человека нет в таблице'

        @allure.title("Update person info in the table")
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "Возраст не был обновлён"

        @allure.title("Delete person from the table")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == 'No rows found', 'человек не был удалён'

        @allure.title("Change number of rows in the table")
        def test_rows_dropdown(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            expected_rows_count = [5, 10, 20]
            rows_count = web_table_page.select_from_rows_dropdown()
            assert rows_count == expected_rows_count, "Количество строк в таблице не изменилось или изменилось некорректно."

    @allure.feature("Buttons")
    class TestButtonsPage:
        @allure.title("Double click button test")
        def test_double_click_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            actual_message = button_page.perform_double_click_button()
            expected_message = "You have done a double click"
            assert actual_message == expected_message, f"Ожидалось сообщение после двойного клика: '{expected_message}', но получено: '{actual_message}'."

        @allure.title("Right click button test")
        def test_right_click_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            actual_message = button_page.perform_right_click_button()
            expected_message = "You have done a right click"
            assert actual_message == expected_message, f"Ожидалось сообщение после правого клика: '{expected_message}', но получено: '{actual_message}'."

        @allure.title("Dynamic click button test")
        def test_click_me_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            actual_message = button_page.perform_click_button()
            expected_message = "You have done a dynamic click"
            assert actual_message == expected_message, f"Ожидалось сообщение после обычного клика: '{expected_message}', но получено: '{actual_message}'."

    @allure.feature("Links")
    class TestLinksPage:

        @allure.title('Checking the link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_home_link()
            assert href_link == current_url, "Ссылка ведет на другой URL или нерабочая"

        @allure.title("API calls test")
        def test_api_calls(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            expected_status_message = links_page.get_api_call_links_text()
            response_code, response_message = links_page.check_api_call_links()
            expected_status_code = links_page.send_calls_get_status_code()
            for k, v in zip(expected_status_message, response_message):
                assert k in v, 'Validating that response message corresponds to link text'
            assert response_code == expected_status_code, 'Validating that status code corresponds to URL status code'

    @allure.feature("Upload and Download")
    class TestUploadAndDownloadPage:

        @allure.title("Upload file test")
        # @pytest.mark.usefixtures("chrome_only")
        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            expected_name = upload_page.upload_file()
            actual_name = upload_page.get_uploaded_file_name()
            assert expected_name == actual_name, \
                f"Ожидалось: {expected_name}, загружено: {actual_name}"

        @allure.title("Download file test")
        def test_download_file(self, driver):
            download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True, "Файл не был скачан"

    @allure.feature("Dynamic Properties")
    class TestDynamicPropertiesPage:

        @allure.title("Test button becomes enabled")
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'Кнопка не включилась'

        @allure.title("Test button color changes")
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_after, color_before = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before, 'Цвет не изменился'

        @allure.title("Test button appears after delay")
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, 'Кнопка не появилась'
