import time
import pytest
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolsTipsPage, MenuPage


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


class TestSliderPage:

    def test_slider_change_value(self,driver):
        slider = SliderPage(driver, "https://demoqa.com/slider")
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after, 'Значение слайдера не изменилось'



class TestProgressBarPage:
    def test_progress_bar(self,driver):
        progress_bar = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()
        assert before != after, 'Значение слайдера не изменилось'


class TestTabsPage:

    def test_tabs(self,driver):
        tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content = tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        more_button, more_content =tabs_page.check_tabs('more')
        assert what_button == 'What' and what_content != 0, 'Неправильный заголовок или отсутствующий текст'
        assert origin_button == 'Origin' and origin_content != 0, 'Неправильный заголовок или отсутствующий текст'
        assert use_button == 'Use' and use_content != 0, 'Неправильный заголовок или отсутствующий текст'
        assert more_button == 'More' and more_content != 0, 'Неправильный заголовок или отсутствующий текст'


class TestToolsTips:

    def test_tooltips(self,driver):
        tool_tips_page = ToolsTipsPage(driver, "https://demoqa.com/tool-tips")
        tool_tips_page.open()
        button_text,field_text, contrary_text,section_text = tool_tips_page.check_tooltips()
        assert button_text == 'You hovered over the Button', 'Hover отсутствует или неверное содержание'
        assert field_text == 'You hovered over the text field', 'Hover отсутствует или неверное содержание'
        assert contrary_text == 'You hovered over the Contrary', 'Hover отсутствует или неверное содержание'
        assert section_text == 'You hovered over the 1.10.32', 'Hover отсутствует или неверное содержание'



class TestMenuPage:

    def test_menu_items(self,driver):
        menu_page = MenuPage(driver, "https://demoqa.com/menu")
        menu_page.open()
        result = menu_page.check_menu()
        print(result)
        assert result == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], 'Не все пункты отображаются'





