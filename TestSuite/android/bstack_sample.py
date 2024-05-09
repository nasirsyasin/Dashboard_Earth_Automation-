import pytest

from TestSuite.Test_Suite_Smoke import test_suite


@pytest.mark.usefixtures('setWebdriver')
class TestSample:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TestSample, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    run = test_suite()
    run.refresh_app()
    run.test_login()
    run.test_AllowNotify()
    run.refresh_app()
    run.test_tooltips()
    run.test_trackAction()
    run.test_compost()
    run.test_ewaste()
    run.mixpanel_export()
    run.compost_verify()
    run.ewaste_verify()

    # def test_example(self):
    #     search_element = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    #     )
    #
    #     search_element.click()
    #     search_input = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    #     )
    #     search_input.send_keys("BrowserStack")
    #     time.sleep(5)
    #     search_results = self.driver.find_elements(
    #         AppiumBy.CLASS_NAME, "android.widget.TextView")
    #
    #     assert len(search_results) > 0
