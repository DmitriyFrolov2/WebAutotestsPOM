from pages.interactions_page import SortablePage


class TestSortablepage:

    def test_sortable(self,driver):
        sortable_page = SortablePage(driver,'https://demoqa.com/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.drag_sortable_item_in_list()
        grid_before, grid_after = sortable_page.drag_sortable_item_in_grid()
        assert list_before != list_after, 'Порядок списка не был изменен'
        assert grid_before != grid_after, 'Порядок сетки не был изменен'


