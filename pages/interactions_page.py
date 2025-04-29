import random

from locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()


    def get_sortable_items(self,elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]


    def drag_sortable_item_in_list(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEMS)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEMS), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what,item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEMS)
        return order_before, order_after


    def drag_sortable_item_in_grid(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEMS)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEMS), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what,item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEMS)
        return order_before, order_after
