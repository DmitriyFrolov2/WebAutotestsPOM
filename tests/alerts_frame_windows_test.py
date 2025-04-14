from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:
        def test_new_tab(self,driver):
            browser_win_page = BrowserWindowsPage(driver,"https://demoqa.com/browser-windows")
            browser_win_page.open()
            text_result = browser_win_page.check_opened_new_tub()
            assert text_result == 'This is a sample page'



        def test_new_window(self,driver):
            new_win_page = BrowserWindowsPage(driver,"https://demoqa.com/browser-windows")
            new_win_page.open()
            text_result = new_win_page.check_opened_new_window()
            assert text_result == 'This is a sample page'
