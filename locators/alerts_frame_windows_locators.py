from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.XPATH,"//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.XPATH,"//button[@id='windowButton']")
    TITLE_NEW_TAB = (By.XPATH,"//h1[@id='sampleHeading']")


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.XPATH,"//button[@id='alertButton']")
    APPEAR_ALERT_BUTTON = (By.XPATH,"//button[@id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.XPATH,"//button[@id='confirmButton']")
    CONFIRM_ALERT_RESULT = (By.XPATH,"//span[@id='confirmResult']")
    PROMPT_ALERT_BUTTON = (By.XPATH,"//button[@id='promtButton']")
    PROMPT_ALERT_RESULT = (By.XPATH,"//span[@id='promptResult']")


class FramesPageLocators:
    FIRST_FRAME = (By.XPATH,"//iframe[@id='frame1']")
    SECOND_FRAME = (By.XPATH,"//iframe[@id='frame2']")
    TITLE_FRAME = (By.XPATH, "//h1[@id='sampleHeading']")
