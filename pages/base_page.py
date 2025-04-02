from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """
        Открывает URL-адрес, связанный с этой страницей, в браузере.
        """
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """
        Проверяет, виден ли элемент на странице в течение заданного времени ожидания.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """
        Проверяет, видны ли все элементы, соответствующие локатору, на странице в течение заданного времени ожидания..
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        Проверяет, присутствует ли элемент в DOM-дереве страницы в течение заданного времени ожидания.
        Не обязательно, чтобы элемент был видимым.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Проверяет, присутствуют ли все элементы, соответствующие локатору, в DOM-дереве страницы в течение заданного времени ожидания.
        Не обязательно, чтобы элементы были видимыми.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """
        Проверяет, что элемент не виден на странице в течение заданного времени ожидания.
        """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        """
        Проверяет, является ли элемент кликабельным на странице в течение заданного времени ожидания.
        Элемент должен быть видимым и доступным для взаимодействия.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Прокручивает страницу до указанного элемента, чтобы сделать его видимым.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        """
        Выполняет двойной щелчок мышью по указанному элементу.
        """
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        """
        Выполняет щелчок правой кнопкой мыши по указанному элементу.
        """
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        """
        Выполняет перетаскивание элемента на заданное смещение (координаты x и y).

        Args:
            x_coords: Смещение по оси X.
            y_coords: Смещение по оси Y.
        """
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_drag_and_drop_to_element(self, what, where):
        """
        Выполняет перетаскивание одного элемента на другой элемент.

        Args:
            what: Веб-элемент, который нужно перетащить.
            where: Веб-элемент, на который нужно перетащить первый элемент.
        """
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def action_move_to_element(self, element):
        """
        Перемещает курсор мыши к центру указанного элемента.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def remove_footer(self):
        """
        Удаляет элементы 'footer' и 'close-fixedban' со страницы с помощью JavaScript.
        """
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")
