import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton


class AllowNotify:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AllowNotify, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.xpath_map = {
            # android xpath
            "notif_allow": '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]',
            # ios xpath
            "i_allow_app": '(//XCUIElementTypeOther[@name="Horizontal scroll bar, 1 page"])[2]',
            "i_notify_allow": '//XCUIElementTypeButton[@name="Allow"]'
        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    def allow_notif(self):
        try:
            self.find_element("notif_allow").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def i_allow_app(self):
        try:
            self.find_element("i_allow_app").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def allow_app_notify(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_allow_app").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("notif_allow").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("allow notification element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def app_refresh(self):
        try:
            self.driver.close_app()
            self.driver.launch_app()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def is_ios(self):
        platform_name = self.driver.capabilities['platformName']
        return platform_name.lower() == 'ios'

    def is_android(self):
        platform_name = self.driver.capabilities['platformName']
        return platform_name.lower() == 'android'


if __name__ == "__main__":
    pytest.main()
    run = AllowNotify()
    run.allow_app_notify()
