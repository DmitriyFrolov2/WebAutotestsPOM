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
    # Locators for the registration a new user
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # Locators for the table

    FULL_PERSON_LIST = (By.XPATH, "//div[@class = 'rt-tr-group']")
    DELETE_BUTTON = (By.XPATH, "//span[@title='Delete']")
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@class = 'rt-tr-group']")
    NO_ROWS_FOUND = (By.XPATH, "//div[@class ='rt-noData']")
    COUNT_ROW_LIST = (By.XPATH, "//select[@aria-label = 'rows per page']")

    #update
    UPDATE_BUTTON = (By.XPATH, "//span[@title='Edit']")

    # Locator for the search
    SEARCH_INPUT = (By.XPATH, "//input[@id='searchBox']")



class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']" )
    # result
    DOUBLE_CLICK_MESSAGE = (By.XPATH, "//p[@id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.XPATH, "//p[@id='rightClickMessage']")
    CLICK_MESSAGE = (By.XPATH, "//p[@id='dynamicClickMessage']")


class LinksPageLocators:
    # Links that navigate
    SIMPLE_LINK = (By.XPATH, "//a[@id='simpleLink']") # Home
    DYNAMIC_LINK = (By.XPATH, "//a[@id='dynamicLink']") # HomeXXXX

    # Links that trigger API calls
    CREATED_LINK = (By.XPATH, "//a[@id='created']")
    NO_CONTENT_LINK = (By.XPATH, "//a[@id='no-content']")
    MOVED_LINK = (By.XPATH, "//a[@id='moved']")
    BAD_REQUEST_LINK = (By.XPATH, "//a[@id='bad-request']")
    UNAUTHORIZED_LINK = (By.XPATH, "//a[@id='unauthorized']")
    FORBIDDEN_LINK = (By.XPATH, "//a[@id='forbidden']")
    NOT_FOUND_LINK = (By.XPATH, "//a[@id='invalid-url']")

    # Output area
    LINK_RESPONSE = (By.XPATH, "//p[@id='linkResponse']")


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By.XPATH, "//input[@id='uploadFile']")
    UPLOADED_RESULT = (By.XPATH, "//p[@id='uploadedFilePath']")

    DOWNLOAD_FILE = (By.XPATH, "//a[@id='downloadButton']")


class DynamicPropertiesPageLocators:
    ENABLE_BUTTON = (By.XPATH, "//button[@id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.XPATH, "//button[@id='colorChange']")
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.XPATH, "//button[@id='visibleAfter']")
