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
            "TrackAction_btn": '//android.view.ViewGroup[@content-desc="Track Actions"]',
            "notif_allow": '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]',
            "tooltip_1_nxt_btn": '//android.view.ViewGroup[@content-desc="Next"]',
            "tooltip_2_done": '//android.view.ViewGroup[@content-desc="Done"]'
        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    # def allow_notif(self):
    #     try:
    #         self.find_element("notif_allow").click()
    #         return True
    #     except Exception as e:
    #         print(f"Exception occurred: {e}")
    #         return False
    # time.sleep(3)
    #
    # def tooltip_1_nxt(self):
    #     try:
    #         self.find_element("tooltip_1_nxt_btn").click()
    #         return True
    #     except Exception as e:
    #         print(f"Exception occurred: {e}")
    #         return False
    #
    # time.sleep(3)
    #
    # def tooltip_2_done(self):
    #     try:
    #         self.find_element("tooltip_2_done").click()
    #         return True
    #     except Exception as e:
    #         print(f"Exception occurred: {e}")
    #         return False

    time.sleep(3)

    def trackActions(self):
        try:
            self.find_element("TrackAction_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def is_ios(self):
        platform_name = self.driver.desired_capabilities['platformName']
        return platform_name.lower() == 'ios'

    def is_android(self):
        platform_name = self.driver.desired_capabilities['platformName']
        return platform_name.lower() == 'android'
