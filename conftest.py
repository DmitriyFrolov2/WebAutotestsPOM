import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# Путь к заранее созданному Firefox-профилю с установленным uBlock Origin
EXTENSIONS_DIR = Path(__file__).parent / "extensions"
FIREFOX_PROFILE_PATH = EXTENSIONS_DIR / "profiles" / "firefox"

PROJECT_ROOT = Path(__file__).resolve().parent
DOWNLOADS_DIR = PROJECT_ROOT / "tests" / "downloads"
PICTURE_PATH = DOWNLOADS_DIR / "picture.jpg"

# Настройки для скачивания файлов
preferences = {
    "download.default_directory": str(Path.cwd() / "downloads"),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "browser.helperApps.neverAsk.saveToDisk": "*/*",
}


# Добавляем пользовательскую опцию запуска браузера
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",  # по умолчанию запускается Firefox
    )


# Фикстура для ручной установки Chrome как браузера. @pytest.mark.usefixtures("chrome_only")
@pytest.fixture()
def chrome_only(request):
    request.config._browser = "chrome"


# Основная фикстура создания и управления драйвером
@pytest.fixture(scope="function")
def driver(request):
    browser_name = getattr(request.config, "_browser", request.config.getoption("--browser"))
    driver = None

    if browser_name == "firefox":
        options = FirefoxOptions()
        #options.binary_location = "/usr/bin/firefox" - для Linux

        # Указываем путь к профилю через аргумент командной строки
        options.add_argument("-profile")
        options.add_argument(str(FIREFOX_PROFILE_PATH))

        # Устанавливаем настройки скачивания через options
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", preferences["download.default_directory"])
        options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               preferences["browser.helperApps.neverAsk.saveToDisk"])

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser_name == "chrome":
        options = ChromeOptions()
        chrome_prefs = {
            "download.default_directory": preferences["download.default_directory"],
            "download.prompt_for_download": preferences["download.prompt_for_download"],
            "safeBrowse.enabled": True
        }
        options.add_experimental_option("prefs", chrome_prefs)

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    if not driver:
        pytest.fail(f"Не удалось инициализировать драйвер для браузера: {browser_name}")

    driver.implicitly_wait(10)

    try:
        yield driver
    finally:
        driver.quit()
