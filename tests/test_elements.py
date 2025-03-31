import pytest
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage


class TestTextBox:

    @pytest.mark.usefixtures("chrome_only")
    def test_text_box(self,driver):
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