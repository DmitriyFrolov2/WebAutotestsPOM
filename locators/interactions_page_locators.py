from selenium.webdriver.common.by import By

class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEMS = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")

    GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEMS = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    LIST_ITEMS = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] li")
    SELECTED_LIST_ITEMS = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")

    GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEMS = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] li")
    SELECTED_GRID_ITEMS = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = (By.XPATH, "//*[@id='resizableBoxWithRestriction']/span")

    RESIZABLE_OBJECT = (By.CSS_SELECTOR, "div[id='resizable']")
    RESIZABLE_OBJECT_HANDLE = (By.XPATH, "//*[@id='resizable']/span")


class DroppablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    SIMPLE_DRAGGABLE = (By.CSS_SELECTOR, "div[id='draggable']")
    SIMPLE_DROPPABLE = (By.CSS_SELECTOR, "#simpleDropContainer #droppable")

    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.CSS_SELECTOR, "div[id='acceptable']")
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, "div[id='notAcceptable']")
    ACCEPT_BOX = (By.CSS_SELECTOR, "#droppableExample-tabpane-accept #droppable")

    PREVENT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    DRAG_BOX = (By.CSS_SELECTOR, "div[id='dragBox']")
    NON_GREEDY_OUTER = (By.CSS_SELECTOR, "div[id='notGreedyDropBox']>p")
    NON_GREEDY_INNER = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']>p")
    GREEDY_OUTER = (By.CSS_SELECTOR, "div[id='greedyDropBox']>p")
    GREEDY_INNER = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']>p")

    REVERT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    REVERT_BOX = (By.CSS_SELECTOR, "div[id='revertable']")
    NON_REVERT_BOX = (By.CSS_SELECTOR, "div[id='notRevertable']")
    REVERT_DROPPABLE = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")


class DraggablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-simple']")
    DRAG_BOX = (By.CSS_SELECTOR, "div[id='dragBox']")

    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    DRAG_BOX_ONLY_Y = (By.CSS_SELECTOR, "div[id='restrictedX']")
    DRAG_BOX_ONLY_X = (By.CSS_SELECTOR, "div[id='restrictedY']")

    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-containerRestriction']")
    RESTRICTIVE_CONTAINER = (By.CSS_SELECTOR, "div[id='containmentWrapper']")
    RESTRICTED_BOX = (By.CSS_SELECTOR, "div[id='containmentWrapper']>div")
    RESTRICTIVE_WIDGET = (By.CSS_SELECTOR, "div[class='draggable ui-widget-content m-3']")
    RESTRICTED_TEXT = (By.CSS_SELECTOR, "div[class='draggable ui-widget-content m-3']>span")

    CURSOR_STYLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-cursorStyle']")
    CURSOR_CENTER = (By.CSS_SELECTOR, "div[id='cursorCenter']")
    CURSOR_TOP_LEFT = (By.CSS_SELECTOR, "div[id='cursorTopLeft']")
    CURSOR_BOTTOM = (By.CSS_SELECTOR, "div[id='cursorBottom']")