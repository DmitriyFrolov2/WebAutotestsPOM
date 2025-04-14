
import time
from pages.form_page import FormPage


class TestFormPage:
    def test_form_page(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        driver.maximize_window()
        submitted_data = form_page.fill_form_fields()
        displayed_results = form_page.form_result()
        assert (displayed_results[0], displayed_results[1]) == \
               (f"{submitted_data.firstname} {submitted_data.lastname}", submitted_data.email)


