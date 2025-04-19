from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, "//div[@id='section1Heading']")
    SECTION_CONTENT_FIRST = (By.XPATH, "//div[@id='section1Content']//p")
    SECTION_SECOND = (By.XPATH, "//div[@id='section2Heading']")
    SECTION_CONTENT_SECOND = (By.XPATH, "//div[@id='section2Content']//p")
    SECTION_THIRD = (By.XPATH, "//div[@id='section3Heading']")
    SECTION_CONTENT_THIRD = (By.XPATH, "//div[@id='section3Content']//p")


class AutocompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
