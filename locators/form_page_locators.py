

from selenium.webdriver.common.by import By


class FormPageLocators:
    # Form locators
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    # GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{randint(1, 3)}']")
    GENDER_MALE = (By.XPATH, "//label[@for='gender-radio-3']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "input[id='gender-radio-2']")
    GENDER_OTHER = (By.CSS_SELECTOR, "input[id='gender-radio-3']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'id="dateOfBirthInput"')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    # HOBBIES = (By.XPATH, "//*[contains(@class, 'custom-checkbox') and .//*[contains(.,'Sports')]]//label")

    HOBBY_SPORT = (By.XPATH, "//*[contains(@class, 'custom-checkbox') and .//*[contains(.,'Sports')]]//label")
    HOBBY_READING = (By.XPATH, "//*[contains(@class, 'custom-checkbox') and .//*[contains(.,'Reading')]]//label")
    HOBBY_MUSIC = (By.XPATH, "//*[contains(@class, 'custom-checkbox') and .//*[contains(.,'Music')]]//label")

    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # table result

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
