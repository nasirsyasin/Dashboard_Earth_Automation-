import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton


class TrackAction:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TrackAction, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.xpath_map = {
            # android xpath
            "TrackAction_btn": '//android.view.ViewGroup[@content-desc="Track an action!"]',
            "tooltip_1_nxt_btn": '//android.view.ViewGroup[@content-desc="Next"]',
            "tooltip_2_done": '//android.view.ViewGroup[@content-desc="Done"]',

            # iOS Xpath
            "i_TrackAction_btn": '//android.view.ViewGroup[@content-desc="Track Actions"]',
            "i_tooltip_nxt1": '(//XCUIElementTypeOther[@name="Next"])[2]',
            "i_tooltip_done2": '(//XCUIElementTypeOther[@name="Done"])[2]'

        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    def tooltip_1_nxt(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_tooltip_nxt1").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("tooltip_1_nxt_btn").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("i_tooltip_nxt1 element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def tooltip_2_done(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_tooltip_done2").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("tooltip_2_done").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("tooltip_2_done element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def trackActions(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_TrackAction_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("TrackAction_btn").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("Track Action element not found for any platform.")
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
    run = TrackAction()
    run.trackActions()
