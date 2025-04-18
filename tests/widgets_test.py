import time

from pages.widgets_page import AccordianPage, AutoCompletePage


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

    def test_fill_single_autocomplete(self,driver):
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

