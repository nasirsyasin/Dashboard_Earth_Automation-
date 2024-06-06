import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton
import time


class MVPCompostPage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MVPCompostPage, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.xpath_map = {
            # android xpath
            "sprout_tooltip": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup',
            "sprout_tooltip_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView',
            "compost_btn": '//android.view.ViewGroup[@content-desc="Compost & Green Bin., +9"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
            "get_started_btn": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]',
            "get_started_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView',
            "explore_climate_link": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]',
            "explore_climate_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView',
            "fork_1_yes_btn": '//android.view.ViewGroup[@content-desc="Yes 1"]',
            "fork_1_yes_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView',
            "fork_2_yes_arrow": '//android.view.ViewGroup[@content-desc="Continue Test1"]',
            "fork_3_yes_arrow": '//android.view.ViewGroup[@content-desc="Continue 2 Test"]',
            "back_arrow_1": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "back_arrow_2": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "fork_1_no_btn": '//android.view.ViewGroup[@content-desc="No 2"]',
            "fork_2_no_arrow": '//android.view.ViewGroup[@content-desc="Continue Test1"]',
            "fork_3_no_arrow": '//android.view.ViewGroup[@content-desc="Continue 2 Test"]',
            "fork_4_no_dropdown": '//android.view.ViewGroup[@content-desc="Choose a place to put your food scraps Testt"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
            "fork_4_no_arrow": '//android.view.ViewGroup[@content-desc="Continue 3"]',
            "compost_action_btn": '//android.view.ViewGroup[@content-desc="Did you separate your food scraps today?, +9"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.RectView',
            "complete_compost": '//android.view.ViewGroup[@content-desc="Continue"]',
            # iOS Locators

            "i_sprout_tooltip": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup',
            "i_sprout_tooltip_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView',
            "i_compost_btn": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View',
            "i_get_started_btn": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]',
            "i_get_started_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView',
            "i_explore_climate_link": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]',
            "i_explore_climate_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView',
            "i_fork_1_yes_btn": '(//XCUIElementTypeOther[@name="YES"])[2]',
            "i_fork_1_yes_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView',
            "i_fork_2_yes_arrow": "(//XCUIElementTypeOther[@name='That's great!  You're already  taking one of the most impactful climate actions in Los Angeles. We'll help you track the impact of your compost — and earn rewards for what you're already doing. Horizontal scroll bar, 1 page'])[20]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther",
            "i_fork_3_yes_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView',
            "i_back_arrow_1": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "i_back_arrow_2": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView',
            "i_fork_1_no_btn": '(//XCUIElementTypeOther[@name="NO"])[2]',
            "i_fork_2_no_arrow": '(//XCUIElementTypeOther[@name="It’s simpler than you think! Tossing food scraps in the green bin is one of the easiest things Angelenos can do to have an impact on climate change.  Horizontal scroll bar, 1 page"])[20]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther',
            "i_fork_3_no_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView',
            "i_fork_4_no_dropdown": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]',
            "i_fork_4_no_arrow": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView',
            "i_compost_action_btn": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View',
            "i_Sometimes_btn": '(//XCUIElementTypeOther[@name="Sometimes"])[2]'

        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    def mvp_compost_btn(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_compost_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("compost_btn").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("compost_btn element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def fork_1_yes_btn(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_1_yes_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_1_yes_btn").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_1_yes_btn element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def fork_2_yes_arrow(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_2_yes_arrow").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_2_yes_arrow").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_2_yes_arrow element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_back_arrow_1(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_back_arrow_1").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("back_arrow_1").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("back_arrow_1 element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_back_arrow_2(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_back_arrow_2").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("back_arrow_2").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("back_arrow_2 element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_1_no_btn(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_1_no_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_1_no_btn").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_1_no_btn element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_2_no_arrow(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_2_no_arrow").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_2_no_arrow").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_2_no_arrow element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_3_no_arrow(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_3_no_arrow").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_3_no_arrow").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_3_no_arrow element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_4_no_open_dropdown(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_4_no_dropdown").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_4_no_dropdown").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_4_no_dropdown element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_4_no_closed_dropdown(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_4_no_dropdown").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_4_no_dropdown").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_4_no_dropdown element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def fork_4_no_arrow(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_fork_4_no_arrow").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("fork_4_no_arrow").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("fork_4_no_arrow element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def compost_action_btn(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_compost_action_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("compost_action_btn").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("compost_action_btn element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    time.sleep(3)

    def complete_compost_action(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_complete_compost").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("complete_compost").click()
                return True

            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("complete_compost element not found for any platform.")
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
    run = MVPCompostPage()
    run.mvp_compost_btn()
    run.fork_1_yes_btn()
    time.sleep(2)
    run.fork_2_yes_arrow()
    time.sleep(2)
    run.fork_back_arrow_1()
    time.sleep(2)
    run.fork_back_arrow_2()
    time.sleep(2)
    run.fork_1_no_btn()
    time.sleep(2)
    run.fork_2_no_arrow()
    time.sleep(2)
    run.fork_3_no_arrow()
    time.sleep(2)
    run.fork_4_no_open_dropdown()
    time.sleep(2)
    run.fork_4_no_closed_dropdown()
    time.sleep(2)
    run.fork_4_no_arrow()
    time.sleep(2)
    run.compost_action_btn()
    time.sleep(2)
    run.complete_compost_action()
