import pytest
import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Настройки для браузеров
preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads"),
    "download.prompt_for_download": False,  # Отключить диалог подтверждения
    "download.directory_upgrade": True  # Разрешить изменение пути загрузки
}

# Функция для добавления пользовательских параметров запуска pytest
def pytest_addoption(parser):
    # Добавляем опцию командной строки --browser
    parser.addoption(
        "--browser",  # имя параметра
        action="store",  # действие - сохранить значение
        default="firefox",  # значение по умолчанию
        help="browser to run tests (firefox or chrome)"  # текст помощи
    )

# Фикстура для установки браузера в Chrome. Синтаксис @pytest.mark.usefixtures("chrome_only")
@pytest.fixture()
def chrome_only(request):
    request.config._browser = "chrome"

# Фикстура для создания и управления браузером
@pytest.fixture(scope="function")  # фикстура будет выполняться для каждой тестовой функции
def driver(request):  # request - специальный объект pytest для доступа к параметрам
    # Получаем значение параметра --browser из командной строки или из chrome_only
    browser_name = getattr(request.config, "_browser", request.config.getoption("--browser"))
    driver = None

    # Создаем драйвер в зависимости от выбранного браузера
    if browser_name == "firefox":
        # Настройки Firefox
        options = FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)  # Использовать кастомный путь
        options.set_preference("browser.download.dir", preferences["download.default_directory"])
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "*/*")  # Автоподтверждение загрузки
        # Устанавливаем GeckoDriver для Firefox
        service = Service(GeckoDriverManager().install())
        # Создаем экземпляр Firefox
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option("prefs", preferences)

        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service as ChromeService
        # Устанавливаем ChromeDriver и создаем экземпляр Chrome
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  options=options)
    else:
        # Выбрасываем исключение, если браузер не поддерживается
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Устанавливаем неявное ожидание (ожидание по умолчанию для поиска элементов)
    driver.implicitly_wait(10)

    try:
        # Передаем драйвер в тест
        yield driver
    finally:
        # Гарантированно закрываем браузер после завершения теста
        driver.quit()
