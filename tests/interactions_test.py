import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.feature('Sortable Page')
class TestSortablePage:

    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.change_list_order()
        grid_before, grid_after = sortable_page.change_grid_order()
        assert list_before != list_after, 'порядок списка не изменился'
        assert grid_before != grid_after, 'порядок сетки не изменился'

@allure.feature('Selectable Page')
class TestSelectablePage:
    @allure.title('Check changed sortable list and grid')
    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_page.open()
        item_list = selectable_page.select_list_item()
        item_grid = selectable_page.select_grid_item()
        assert len(item_list) > 0, "не выбрано ни одного элемента"
        assert len(item_grid) > 0, "не выбрано ни одного элемента"

@allure.feature('Resizable Page')
class TestResizablePage:
    @allure.title('Check changed resizable boxes')
    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
        max_box, min_box = resizable_page.change_size_resizable_box()
        max_resize, min_resize = resizable_page.change_size_resizable()
        assert ('500px', '300px') == max_box, "максимальный размер не равен '500px', '300px'"
        assert ('150px', '150px') == min_box, "минимальный размер не равен '150px', '150px'"
        assert min_resize != max_resize, "размер изменяемого элемента не изменился"

@allure.feature('Droppable Page')
class TestDroppablePage:
    @allure.title('Check simple droppable')
    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!', "элемент не был сброшен"

    @allure.title('Check accept droppable')
    def test_accept_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        not_accept, accept = droppable_page.drop_accept()
        assert not_accept == 'Drop here', "сброшенный элемент был принят"
        assert accept == 'Dropped!', "сброшенный элемент не был принят"

    @allure.title('Check revert draggable droppable')
    def test_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
        not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
        assert will_after_move != will_after_revert, 'элемент не вернулся в исходное положение'
        assert not_will_after_move == not_will_after_revert, 'элемент вернулся в исходное положение'

@allure.feature('Draggable Page')
class TestDraggablePage:
    @allure.title('Check simple draggable')
    def test_simple_draggable(self, driver):
        draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
        draggable_page.open()
        before, after = draggable_page.simple_drag_box()
        assert before != after, "позиция блока не изменилась"

    @allure.title('Check axis restricted draggable')
    def test_axis_restricted_draggable(self, driver):
        draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
        draggable_page.open()
        top_x, left_x = draggable_page.axis_restricted_x()
        top_y, left_y = draggable_page.axis_restricted_y()
        assert top_x[0][0] == top_x[1][0] and int(
            top_x[1][0]) == 0, "позиция блока не изменилась или произошло смещение по оси Y"
        assert left_x[0][0] != left_x[1][0] and int(
            left_x[1][0]) != 0, "позиция блока не изменилась или произошло смещение по оси Y"
        assert top_y[0][0] != top_y[1][0] and int(
            top_y[1][0]) != 0, "позиция блока не изменилась или произошло смещение по оси X"
        assert left_y[0][0] == left_y[1][0] and int(
            left_y[1][0]) == 0, "позиция блока не изменилась или произошло смещение по оси X"