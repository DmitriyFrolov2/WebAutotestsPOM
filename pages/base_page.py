from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import requests
from selenium.webdriver.support.wait import WebDriverWait


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

        present_element = self.element_is_present(locator, timeout) # Сначала убедимся, что элемент есть в DOM
        if present_element:
             self.go_to_element(present_element)
             try:
                 return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
             except TimeoutException:
                 print(f"Элемент не стал видимым за {timeout} секунд по локатору: {locator}")
                 return None
        else:
             print(f"Элемент не найден в DOM для проверки видимости: {locator}")
             return None


    def elements_are_visible(self, locator, timeout=5):
        """
        Проверяет, видны ли все элементы, соответствующие локатору, на странице в течение заданного времени ожидания.
        """
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Не все элементы стали видимыми за {timeout} секунд по локатору: {locator}")
            return [] # Возвращаем пустой список при тайм-ауте

    def element_is_present(self, locator, timeout=5):
        """
        Проверяет, присутствует ли элемент в DOM-дереве страницы в течение заданного времени ожидания.
        Не обязательно, чтобы элемент был видимым.
        """
        try:
            return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент не появился в DOM за {timeout} секунд по локатору: {locator}")
            return None

    def elements_are_present(self, locator, timeout=5):
        """
        Проверяет, присутствуют ли все элементы, соответствующие локатору, в DOM-дереве страницы в течение заданного времени ожидания.
        Не обязательно, чтобы элементы были видимыми.
        """
        try:
            return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Не все элементы появились в DOM за {timeout} секунд по локатору: {locator}")
            return []

    def element_is_not_visible(self, locator, timeout=5):
        """
        Проверяет, что элемент не виден (или отсутствует в DOM) на странице в течение заданного времени ожидания.
        """
        try:
            return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
             # Если элемент так и не стал невидимым (т.е. остался видимым или не появился),
             # то условие не выполнилось. В зависимости от логики, можно вернуть False или поднять ошибку.
             print(f"Элемент остался видимым или не появился за {timeout} секунд по локатору: {locator}")
             return False # Условие невидимости не выполнено

    def element_is_clickable(self, locator, timeout=10):
        """
        Проверяет, является ли элемент кликабельным на странице в течение заданного времени ожидания.
        Элемент должен быть видимым и доступным для взаимодействия.
        """
        try:
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Элемент не стал кликабельным за {timeout} секунд по локатору: {locator}")
            return None

    def go_to_element(self, element):
        """
        Прокручивает страницу до указанного элемента, чтобы сделать его видимым.
        """
        # Проверяем, что element не None перед прокруткой
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        else:
            print("Невозможно прокрутить к элементу: элемент не найден (None).")

    def click_element(self, locator, timeout=10):
        element = self.element_is_visible(locator, timeout)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()


    def action_double_click(self, element):
        """
        Выполняет двойной щелчок мышью по указанному элементу.
        """
        # Добавим проверку, что элемент существует
        if element:
            action = ActionChains(self.driver)
            action.double_click(element)
            action.perform()
        else:
            print("Невозможно выполнить двойной клик: элемент не найден (None).")


    def action_right_click(self, element):
        """
        Выполняет щелчок правой кнопкой мыши по указанному элементу.
        """
        if element:
            action = ActionChains(self.driver)
            action.context_click(element)
            action.perform()
        else:
             print("Невозможно выполнить правый клик: элемент не найден (None).")

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        """
        Выполняет перетаскивание элемента на заданное смещение (координаты x и y).

        Args:
            element: Веб-элемент для перетаскивания.
            x_coords: Смещение по оси X.
            y_coords: Смещение по оси Y.
        """
        if element:
            action = ActionChains(self.driver)
            action.drag_and_drop_by_offset(element, x_coords, y_coords)
            action.perform()
        else:
            print("Невозможно выполнить drag and drop: элемент не найден (None).")

    def action_drag_and_drop_to_element(self, what, where):
        """
        Выполняет перетаскивание одного элемента на другой элемент.

        Args:
            what: Веб-элемент, который нужно перетащить.
            where: Веб-элемент, на который нужно перетащить первый элемент.
        """
        if what and where:
            action = ActionChains(self.driver)
            action.drag_and_drop(what, where)
            action.perform()
        else:
             print("Невозможно выполнить drag and drop: один или оба элемента не найдены (None).")


    def action_move_to_element(self, element):
        """
        Перемещает курсор мыши к центру указанного элемента.
        """
        if element:
            action = ActionChains(self.driver)
            action.move_to_element(element)
            action.perform()
        else:
            print("Невозможно переместить курсор: элемент не найден (None).")

    def remove_footer(self):

        self.driver.execute_script("document.getElementByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")

    def get_status_code(self, url, timeout=10):
        """
        Отправляет GET-запрос на указанный URL и возвращает его HTTP статус-код.
        Использует библиотеку requests. Включает User-Agent и обработку исключений.

        Args:
            url (str): URL для проверки.
            timeout (int): Время ожидания ответа в секундах.

        Returns:
            int | None: Статус-код HTTP или None в случае ошибки запроса.
        """
        try:
            """Можно добавить User-Agent, чтобы имитировать браузер и уменьшить вероятность блокировки
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }"""
            response = requests.get(url, timeout=timeout) #headers=headers, allow_redirects=True, verify=False  verify=False может быть нужен для self-signed сертификатов
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении GET-запроса к URL '{url}': {e}")
            return None # Возвращаем None при любой ошибке запроса

    def get_element_text(self, locator, timeout=5):
        """
        Ожидает видимости элемента и возвращает его текст.

        Args:
            locator: Локатор элемента (например, (By.ID, "myElement")).
            timeout (int): Максимальное время ожидания элемента.

        Returns:
            str | None: Текст элемента или None, если элемент не найден или не имеет текста.
        """
        try:
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            print(f"Элемент не стал видимым для получения текста за {timeout} секунд по локатору: {locator}")
            return None


    def get_current_url(self):
        """
        Возвращает URL текущей активной вкладки/окна.
        """
        return self.driver.current_url

    def execute_script(self, script, *args):
        """
        Выполняет переданный JavaScript в контексте текущего окна или фрейма.
        Это обертка для стандартного метода execute_script драйвера.
        """

    def go_to_alert(self):
        return self.driver.switch_to.alert

    def go_to_new_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])


    def go_to_frame(self, locator):
        self.driver.switch_to.frame(locator)


    def go_to_default_content(self):
        self.driver.switch_to.default_content()


    def select_option_by_text(self, locator, value):
        select = Select(self.element_is_present(locator))
        select.select_by_visible_text(value)



