import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton


# @pytest.mark.usefixtures('setWebdriver')
class LoginPage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoginPage, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.xpath_map = {
            "login_link": '//android.view.ViewGroup[@content-desc="Log in"]/android.widget.TextView',
            "email_input": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]",
            "password_input": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]",
            "login_btn": '//android.view.ViewGroup[@content-desc="Log in"]',
            # iOS app xpath
            "iOS_allow_popup": '//XCUIElementTypeButton[@name="Allow"]',
            "i_login_link": '//XCUIElementTypeOther[@name="Log in"]',
            "i_email_input": '(//XCUIElementTypeOther[@name="Enter email "])[2]/XCUIElementTypeTextField',
            "i_password_input": '//XCUIElementTypeOther[@name="Enter password"]/XCUIElementTypeSecureTextField',
            "i_login_btn": '//XCUIElementTypeOther[@name="Log in"]'

        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver
        # self.is_ios = Platforms().is_ios
        # self.is_android = Platforms().is_android

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    # def allow_popup(self):
    #     try:
    #         self.find_element("iOS_allow").click()
    #         return True
    #     except Exception as e:
    #         print(f"Exception occurred: {e}")
    #         return False

    def login_link(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("iOS_allow_popup").click()
                self.find_element("i_login_link").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("login_link").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("Login link element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def email_input(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                email_input = self.find_element("i_email_input")
                email_input.clear()
                email_input.send_keys("zubair.shahid+11660@mavrictech.com")
                return True

            # Check for Android specific elements
            elif self.is_android():
                email_input = self.find_element("email_input")
                email_input.clear()
                email_input.send_keys("zubair.shahid+11660@mavrictech.com")
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("email_input element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def password_input(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                password_input = self.find_element("i_password_input")
                password_input.clear()
                password_input.send_keys("P@ss1234")
                return True

            # Check for Android specific elements
            elif self.is_android():
                password_input = self.find_element("password_input")
                password_input.clear()
                password_input.send_keys("P@ss1234")
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("Login link element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def login_btn(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_login_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("login_btn").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("Login link element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def is_ios(self):
        platform_name = self.driver.desired_capabilities['platformName']
        return platform_name.lower() == 'ios'

    def is_android(self):
        platform_name = self.driver.desired_capabilities['platformName']
        return platform_name.lower() == 'android'


if __name__ == "__main__":
    pytest.main()
    pytest.login_link()
