import pytest
from pathlib import Path
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

# Пути к расширениям AdBlock
EXTENSIONS_DIR = Path(__file__).parent / "extensions"  # Папка extensions в корне проекта
ADBLOCK_CHROME = EXTENSIONS_DIR / "adblock_chrome.crx"  # Путь к расширению для Chrome
ADBLOCK_FIREFOX = EXTENSIONS_DIR / "adblock_firefox.xpi"  # Путь к расширению для Firefox

# Настройки для браузеров
preferences = {
    "download.default_directory": str(Path.cwd() / "downloads"),  # Кросс-платформенный путь
    "download.prompt_for_download": False,  # Отключить диалог подтверждения
    "download.directory_upgrade": True,  # Разрешить изменение пути загрузки
    "browser.helperApps.neverAsk.saveToDisk": "*/*",  # Автоподтверждение загрузки для всех типов
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
    options = None  # Объявляем переменную заранее

    # Создаем драйвер в зависимости от выбранного браузера
    if browser_name == "firefox":
        # Настройки Firefox
        options = FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)  # Использовать кастомный путь
        options.set_preference("browser.download.dir", preferences["download.default_directory"])
        options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               preferences["browser.helperApps.neverAsk.saveToDisk"])  # Автоподтверждение загрузки

        # Устанавливаем GeckoDriver для Firefox
        service = Service(GeckoDriverManager().install())
        # Создаем экземпляр Firefox
        driver = webdriver.Firefox(service=service, options=options)

        # Добавляем AdBlock если файл существует
        if ADBLOCK_FIREFOX.exists() and ADBLOCK_FIREFOX.is_file():
            try:
                # Устанавливаем расширение временно для текущей сессии
                driver.install_addon(str(ADBLOCK_FIREFOX), temporary=True)
                # Даем время расширению на инициализацию (особенно AdBlock)
                time.sleep(4)
            except Exception:
                # Расширение не установилось, можно добавить логирование или pytest.fail()
                # print(f"Предупреждение: Не удалось установить расширение Firefox: {e}")
                pass  # Продолжаем выполнение теста без расширения


    elif browser_name == "chrome":
        options = ChromeOptions()
        # Создаем словарь prefs только с нужными для Chrome настройками
        chrome_prefs = {
            "download.default_directory": preferences["download.default_directory"],
            "download.prompt_for_download": preferences["download.prompt_for_download"],
            "safeBrowse.enabled": True  # Пример другой настройки для Chrome
        }
        options.add_experimental_option("prefs", chrome_prefs)  # Применяем настройки

        # Добавляем AdBlock если файл существует (добавлено)
        # Для Chrome метод add_extension через options все еще актуален
        if ADBLOCK_CHROME.exists() and ADBLOCK_CHROME.is_file():
            options.add_extension(str(ADBLOCK_CHROME))

        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service as ChromeService
        # Устанавливаем ChromeDriver и создаем экземпляр Chrome
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # if ADBLOCK_CHROME.exists() and ADBLOCK_CHROME.is_file():
        #     # Если AdBlock в Chrome не успевает блокировать рекламу на первых страницах
        #     time.sleep(10)


    else:
        # Выбрасываем исключение, если браузер не поддерживается
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Проверка, что драйвер был успешно создан ###
    if not driver:
        pytest.fail(f"Не удалось инициализировать драйвер для браузера: {browser_name}")

    # Устанавливаем неявное ожидание (ожидание по умолчанию для поиска элементов)
    driver.implicitly_wait(10)

    try:
        # Передаем драйвер в тест
        yield driver
    finally:
        # Гарантированно закрываем браузер после завершения теста
        if driver:
            driver.quit()
