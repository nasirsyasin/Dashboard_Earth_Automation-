import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton

# Driver initialization
appium_driver_singleton = AppiumDriverSingleton()
appium_driver = appium_driver_singleton.get_driver


class LoginPage:
    _instance = None

    # Ensure only one instance is created
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoginPage, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    # Initialization method
    def _initialize(self):
        self.xpath_login_link = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView'
        self.xpath_email_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]'
        self.xpath_password_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]'
        self.xpath_login_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[8]'
        self.xpath_test = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout'

    # Methods to interact with the login screen
    def login_link(self):
        try:
            WebDriverWait(appium_driver, 100).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_login_link))).click()

            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def email_input(self):
        try:
            login_email_input = WebDriverWait(appium_driver, 100).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_email_input)))
            login_email_input.clear()
            login_email_input.send_keys("zubair.shahid+61976@mavrictech.com")
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def password_input(self):
        try:
            login_password_input = WebDriverWait(appium_driver, 100).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_password_input)))
            login_password_input.clear()
            login_password_input.send_keys("P@ss1234")
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def login_btn(self):
        try:
            WebDriverWait(appium_driver, 100).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_login_btn))).click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False


# if __name__ == "__main__":
#     pytest.main()
#     pytest.LoginPage.login_link()
