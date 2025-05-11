import allure
import pytest
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolsTipsPage, MenuPage, SelectMenuPage


@allure.feature('Accordian Page')
class TestAccordianPage:
    @allure.title('Check accordian widget')
    def test_accordian(self, driver):
        accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
        accordian_page.open()
        FIRST_SECTION_EXPECTED = ["What is Lorem Ipsum?", "Lorem Ipsum is simply dummy text"]
        SECOND_SECTION_EXPECTED = ["Where does it come from?",
                                   "It has roots in a piece of classical Latin literature from 45 BC"]
        THIRD_SECTION_EXPECTED = ["Why do we use it?",
                                  "It is a long established fact that a reader will be distracted"]
        second_section = accordian_page.check_accordian("second")
        third_section = accordian_page.check_accordian("third")
        first_section = accordian_page.check_accordian("first")
        assert first_section[0] == FIRST_SECTION_EXPECTED[0] and FIRST_SECTION_EXPECTED[1] in first_section[1]
        assert second_section[0] == SECOND_SECTION_EXPECTED[0] and SECOND_SECTION_EXPECTED[1] in second_section[1]
        assert third_section[0] == THIRD_SECTION_EXPECTED[0] and THIRD_SECTION_EXPECTED[1] in third_section[1]


@allure.feature('Autocomplete page')
class TestAutoCompletePage:
    @allure.title('Check the autocomplete is filled')
    def test_fill_multi_autocomplete(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        colors = auto_complete_page.fill_input_multi()
        colors_result = auto_complete_page.check_color_in_multi()
        assert colors == colors_result, 'Не все цвета добавились в поле'

    @allure.title('Check deletions from the multiple autocomplete')
    def test_remove_value_from_multi(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        auto_complete_page.fill_input_multi()
        count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
        assert count_value_before != count_value_after, 'Элемент не удален'

    @allure.title('Check clear all from the multiple autocomplete')
    def test_clear_all_from_multi(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        auto_complete_page.fill_input_multi()
        is_removed = auto_complete_page.clear_all_from_multi()
        assert is_removed== True, 'Элемент не удалён'

    @allure.title('Check deletions from the single autocomplete')
    def test_fill_single_autocomplete(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        color = auto_complete_page.fill_input_single()
        color_result = auto_complete_page.check_color_in_single()
        assert color == color_result, 'Не добавился цвет'


@allure.feature('Date Picker Page')
class TestDataPickerPage:
    # @pytest.mark.usefixtures("chrome_only")
    @allure.title('Check change date')
    def test_change_data(self, driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        value_data_before, value_data_after = date_picker_page.select_date()
        assert value_data_before == value_data_after, 'Дата не была изменена'

    @allure.title('Check change date and time')
    def test_change_data_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        date_time_value_before, date_time_value_after = date_picker_page.select_date_and_time()
        assert date_time_value_before != date_time_value_after, 'Дата и время не были изменены'


@allure.feature('Slider Page')
class TestSliderPage:
    @allure.title('Check moved slider')
    def test_slider_change_value(self, driver):
        slider = SliderPage(driver, "https://demoqa.com/slider")
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after, 'Значение слайдера не изменилось'


@allure.feature('Progress Bar Page')
class TestProgressBarPage:
    @allure.title('Check changed progress bar')
    def test_progress_bar(self, driver):
        progress_bar = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()
        assert before != after, 'Значение слайдера не изменилось'


@allure.feature('Test Tabs Page')
class TestTabsPage:
    @allure.title('Check switched tabs')
    @pytest.mark.xfail(reason="Тест не проходит из-за задизейбленной вкладки 'More'.")
    def test_tabs(self, driver):
        tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content = tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        more_button, more_content = tabs_page.check_tabs('more')
        assert what_button == 'What' and what_content != 0, 'Неправильный заголовок или отсутствующий текст'
        assert origin_button == 'Origin' and origin_content != 0, 'Неправильный заголовок или отсутствующий текст'
        assert use_button == 'Use' and use_content != 0, 'Неправильный заголовок или отсутствующий текст'
        assert more_button == 'More' and more_content != 0, 'Неправильный заголовок или отсутствующий текст'


@allure.feature('Tool Tips')
class TestToolsTipsPage:
    @allure.title('Check tool tips ')
    def test_tooltips(self, driver):
        tool_tips_page = ToolsTipsPage(driver, "https://demoqa.com/tool-tips")
        tool_tips_page.open()
        button_text, field_text, contrary_text, section_text = tool_tips_page.check_tooltips()
        assert button_text == 'You hovered over the Button', 'Hover отсутствует или неверное содержание'
        assert field_text == 'You hovered over the text field', 'Hover отсутствует или неверное содержание'
        assert contrary_text == 'You hovered over the Contrary', 'Hover отсутствует или неверное содержание'
        assert section_text == 'You hovered over the 1.10.32', 'Hover отсутствует или неверное содержание'


@allure.feature('MenuPage')
class TestMenuPage:
    @allure.title('Check all menu items are displayed correctly')
    def test_menu_items(self, driver):
        menu_page = MenuPage(driver, "https://demoqa.com/menu")
        menu_page.open()
        result = menu_page.check_menu()
        assert result == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                          'Sub Sub Item 2', 'Main Item 3'], 'Не все пункты отображаются'


@allure.feature('Select Menu Page')
class TestSelectMenuPage:
    @allure.title('Check select value functionality')
    def test_select_value(self, driver):
        select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
        select_menu_page.open()
        select_input_value, select_current_value = select_menu_page.check_select_value()
        assert select_input_value in select_current_value, "Выбранное значение не отображается в поле"

    @allure.title('Check select one value functionality')
    def test_select_one_value(self, driver):
        select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
        select_menu_page.open()
        select_input_one_value, select_current_one_value = select_menu_page.check_select_one_value()
        assert select_input_one_value in select_current_one_value, 'Выбранное значение не отображается в поле'

    @allure.title('Check old style select functionality')
    def test_old_style_select(self, driver):
        select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
        select_menu_page.open()
        selected_text, random_color = select_menu_page.check_old_style_select()
        assert selected_text == random_color, 'Выбранное значение не соответствует ожидаемому'

    @allure.title('Check multi-select values functionality')
    def test_select_multiple_value(self, driver):
        select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
        select_menu_page.open()
        select_values, current_values = select_menu_page.check_multi_select()

        assert set(select_values) == set(current_values), 'Выбранные значения не совпадают с отображаемыми'

    @allure.title('Verify removal of multi-selected values')
    def test_remove_select_multiple_value(self, driver):
        select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
        select_menu_page.open()
        select_menu_page.check_multi_select()
        items_removed_status = select_menu_page.are_multiselected_items_removed()
        assert items_removed_status is True, 'Элементы не удалены'

    @allure.title('Check standard multi-select functionality')
    def test_standart_multiselect(self, driver):
        select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
        select_menu_page.open()

        actual_selected_values, expected_selected_values = select_menu_page.check_standart_multiselect()

        assert actual_selected_values == expected_selected_values, 'Выбранные значения не совпадают с отображаемыми'
