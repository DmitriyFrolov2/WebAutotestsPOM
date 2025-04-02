from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # created from

    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    CHECK_BOXES_ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")
    CHECKED_ITEMS = (By.CLASS_NAME, "rct-icon-check")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # table

    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class = 'rt-tr-group']")