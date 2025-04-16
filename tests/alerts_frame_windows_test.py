from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


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


    class TestAlertsPage:
        def test_see_alert(self,driver):
            alerts_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Предупреждение не появилось"


        def test_check_alert_appear_5_sec(self,driver):
            alerts_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Предупреждение не появилось"


        def test_confirm_alert(self,driver):
            alerts_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text =='You selected Ok', "Предупреждение не появилось"


        def test_dismiss_alert(self,driver):
            alerts_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_dismiss_alert()
            assert alert_text == 'You selected Cancel', "Предупреждение не появилось"


        def test_prompt_alert(self,driver):
            alerts_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_alert()
            assert text in alert_text, "Предупреждение не появилось"


    class TestFramesPage:

        def test_frames(self,driver):
            frame_page = FramesPage(driver,'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame1('frame1')
            result_frame2 = frame_page.check_frame2('frame2')
            assert result_frame1 ==['500px', '350px', 'This is a sample page']
            assert result_frame2 == ['100px', '100px', 'This is a sample page']


    class TestNestedFramesPage:

        def test_nested_frames(self,driver):
            nested_frame_page = NestedFramesPage(driver,'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text =nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame'
            assert child_text =='Child Iframe'




    class TestModalDialogsPage:

        def test_small_modal_dialogs(self,driver):
            small_dialogs_page = ModalDialogsPage(driver,'https://demoqa.com/modal-dialogs')
            small_dialogs_page.open()
            small_title, small_text = small_dialogs_page.check_small_modal_dialogs()
            assert small_title == 'Small Modal', \
                f"Ожидался заголовок 'Small Modal', но получен '{small_title}'"

            assert small_text == 'This is a small modal. It has very less content', \
                f"Ожидался текст 'This is a small modal...', но получен '{small_text}'"


        def test_large_modal_dialogs(self,driver):
            large_dialogs_page = ModalDialogsPage(driver,'https://demoqa.com/modal-dialogs')
            large_dialogs_page.open()
            large_title, large_text = large_dialogs_page.check_large_modal_dialogs()
            assert large_title == 'Large Modal', \
                f"Ожидался заголовок 'Large Modal', но получен '{large_title}'"

            assert len(large_text) > 100, \
                f"Ожидался длинный текст (>100 символов), но получено {len(large_text)} символов"









