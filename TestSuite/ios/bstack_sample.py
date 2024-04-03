import pytest
from Tests.Mobile_Tests.Sign_up_with_email import test_signup_with_email


@pytest.mark.usefixtures('setWebdriver')
class TestSample:
    test_signup_with_email()
    # def test_example(self):
    #     text_button = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
    #     )
    #     text_button.click()
    #     text_input = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
    #     )
    #     text_input.send_keys("hello@browserstack.com"+"\n")
    #     time.sleep(5)
    #     text_output = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
    #     )
    #     assert text_output!=None and text_output.text=="hello@browserstack.com"
