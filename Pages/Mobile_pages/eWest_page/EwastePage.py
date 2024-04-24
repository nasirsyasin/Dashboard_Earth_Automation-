import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton


class EwastePage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EwastePage, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.xpath_map = {
            "ewaste_action_btn": '//android.view.ViewGroup[@content-desc="e-waste MVP, +20"]/com.horcrux.svg.SvgView[2]',
            "ewaste_action_txt": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView[2]",
            "ewaste_yes_txt": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView",
            "ewaste_no_btn": '//android.view.ViewGroup[@content-desc="No"]/android.widget.TextView',
            "ewaste_no_txt": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup",
            "ewaste_not_sure_btn": "//android.view.ViewGroup[@content-desc='I'm not sure']",
            "ewaste_not_sure_txt": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView",
            "ewaste_no_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup',
            "ewaste_no_back_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "ewaste_not_sure_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            # "ewaste_not_sure_back_arrow" : '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
            # "ewaste_yes_arrow" : '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "ewaste_yes_back_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "ewaste_not_sure_back_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "ewaste_yes_btn": '//android.view.ViewGroup[@content-desc="Yes"]/android.widget.TextView',
            "ewaste_yes_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup',
            "ewaste_map_link": '//android.view.ViewGroup[@content-desc="For more info click here →"]/android.widget.TextView',
            "ewaste_photo_upload_btn": '//android.view.ViewGroup[@content-desc="Upload photo."]/android.widget.TextView',
            "ewaste_map_details_cross": '//android.view.ViewGroup[@content-desc=""]',
            "ewaste_cam_btn": '//android.view.ViewGroup[@content-desc=""]',
            "ewaste_camera_btn": '//android.widget.Button[@content-desc="Camera"]',
            "ewaste_camera_permission": '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]',
            "ewaste_camera_capture": '//android.view.ViewGroup[@content-desc="Take picture"]',
            "save_ok_photo": '//android.widget.Button[@content-desc="OK"]/android.view.ViewGroup',
            "verify_complete_btn": '//android.view.ViewGroup[@content-desc="Verify and complete.."]/android.widget.TextView',
            "completed_action_btn": '//android.view.ViewGroup[@content-desc="Complete Action"]',

        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    def ewaste_action_btn(self):
        try:
            self.find_element("ewaste_action_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_no_btn(self):
        try:
            self.find_element("ewaste_no_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_no_arrow(self):
        try:
            self.find_element("ewaste_no_arrow").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_action_btn_not_sure(self):
        try:
            self.find_element("ewaste_action_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    # def ewaste_not_sure_btn(self):
    #     try:
    #         self.find_element("ewaste_not_sure_btn").click()
    #         return True
    #     except Exception as e:
    #         print(f"Exception occurred: {e}")
    #         return False
    #
    # def ewaste_not_sure_back_arrow(self):
    #     try:
    #         self.find_element("ewaste_not_sure_back_arrow").click()
    #         return True
    #     except Exception as e:
    #         print(f"Exception occurred: {e}")
    #         return False

    def ewaste_yes_btn(self):
        try:
            self.find_element("ewaste_yes_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_yes_arrow(self):
        try:
            self.find_element("ewaste_yes_arrow").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_map_link(self):
        try:
            self.find_element("ewaste_map_link").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_map_details_cross(self):
        try:
            self.find_element("ewaste_map_details_cross").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_photo_cap_btn(self):
        try:
            self.find_element("ewaste_photo_upload_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_cam_btn(self):
        try:
            self.find_element("ewaste_photo_upload_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_camera_btn(self):
        try:
            self.find_element("ewaste_camera_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_camera_permission(self):
        try:
            self.find_element("ewaste_camera_permission").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def ewaste_camera_capture(self):
        try:
            self.find_element("ewaste_camera_capture").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def save_ok_photo(self):
        try:
            self.find_element("save_ok_photo").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def verify_complete_btn(self):
        try:
            self.find_element("verify_complete_btn").click()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def completed_action_btn(self):
        try:
            self.find_element("completed_action_btn").click()
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
