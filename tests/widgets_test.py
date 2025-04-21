import time

from pages.widgets_page import AccordianPage, AutoCompletePage,DatePickerPage


class TestAccordianPage:
    def test_accordian(self,driver):
        accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Неправильный заголовок или отсутствующий текст'
        assert second_title == 'Where does it come from?' and second_content > 0, 'Неправильный заголовок или отсутствующий текст'
        assert third_title == 'Why do we use it?' and third_content > 0, 'Неправильный заголовок или отсутствующий текст'


class TestAutoCompletePage:

    def test_fill_multi_autocomplete(self,driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        colors = auto_complete_page.fill_input_multi()
        colors_result = auto_complete_page.check_color_in_multi()
        assert colors == colors_result, 'Не все цвета добавились в поле'



    def test_remove_value_from_multi(self,driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        auto_complete_page.fill_input_multi()
        count_value_before , count_value_after = auto_complete_page.remove_value_from_multi()
        assert count_value_before != count_value_after, 'Элемент не удален'

    def test_clear_all_from_multi(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        auto_complete_page.fill_input_multi()
        is_removed = auto_complete_page.clear_all_from_multi()
        assert is_removed == True, 'Элемент не удалён'


    def test_fill_single_autocomplete(self,driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        color = auto_complete_page.fill_input_single()
        color_result = auto_complete_page.check_color_in_single()
        assert color == color_result, 'Не добавился цвет'


class TestDataPickerPage:
    def test_change_data(self,driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        value_data_before, value_data_after = date_picker_page.select_date()
        assert value_data_before != value_data_after, 'Дата не была изменена'



    def test_change_data_and_time(self,driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        date_time_value_before, date_time_value_after = date_picker_page.select_date_and_time()
        assert date_time_value_before != date_time_value_after, 'Дата и время не были изменены'






