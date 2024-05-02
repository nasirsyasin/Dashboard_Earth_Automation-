import time

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
            "notif_allow": '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'
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

    def app_refresh(self):
        try:
            self.driver.close_app()
            self.driver.launch_app()
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
