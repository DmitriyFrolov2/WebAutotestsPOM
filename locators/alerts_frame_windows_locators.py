from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.XPATH,"//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.XPATH,"//button[@id='windowButton']")


    TITLE_NEW_TAB = (By.XPATH,"//h1[@id='sampleHeading']")