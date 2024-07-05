from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.RandomEmailGenerator import RandomEmailGenerator
from Utility.common_cache import CommonCache
from Utility.mobile_driver_setup import AppiumDriverSingleton


class OnboardingPage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OnboardingPage, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.xpath_map = {
            "get_started_btn": '//android.view.ViewGroup[@content-desc="Continue "]',
            "non_la_sc_back_icon": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView',
            "non_la_link": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView',
            "onboarding_arrow_1": '//android.view.ViewGroup[@content-desc="Continue "]',
            "onboarding_arrow_2": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup',
            "onboarding_arrow_3": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup',
            "onboarding_get_started": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup',
            "onboarding_get_started_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView',
            "sign_up_with_email_btn": '//android.view.ViewGroup[@content-desc="Continue with Email."]',
            "sign_up_with_email_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView',
            "sign_up_with_email_emailsvgicon": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
            "text_btn": "Continue with Email.",
            "sign_up_with_google_btn": '/hierarchy/android.widnget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]',
            "sign_up_with_google_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView',
            "text_sign_up_with_google_btn": 'Continue with Google.',
            "signup_title": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView',
            "input_email_address": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]',
            "input_first_name": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]',
            "input_last_name": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[3]',
            "input_password": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[4]',
            "retype_password": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[5]',
            "sign_up_btn": '//android.view.ViewGroup[@content-desc="Sign Up"]',
            "notif_allow_link": '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]',
            "id_notif_allow_link": 'com.android.permissioncontroller:id/permission_allow_button',
            "sprout_tooltip_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView',
            "sprout_tooltip": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup',
            "compost_tooltip": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]',
            "ewaste_tooltip": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]',
            # iOS locators
            "iOS_allow_popup": '//XCUIElementTypeButton[@name="Allow"]',
            "i_get_started_btn": '(//XCUIElementTypeOther[@name="GET STARTED"])[2]',
            "i_non_la_sc_back_icon": '',
            "i_non_la_link": '(//XCUIElementTypeOther[@name="Don’t live in LA?"])[2]',
            "i_onboarding_arrow_1": '(//XCUIElementTypeOther[@name="Here’s what we know:"])[20]/XCUIElementTypeOther[4]/XCUIElementTypeOther',
            "i_onboarding_arrow_2": '(//XCUIElementTypeOther[@name="In fact, 67% of Americans are feeling climate anxiety. That’s where we come in.. Vertical scroll bar, 1 page Horizontal scroll bar, 1 page"])[20]/XCUIElementTypeOther[4]/XCUIElementTypeOther',
            "i_onboarding_arrow_3": '(//XCUIElementTypeOther[@name="We’re helping Angelenos log their climate actions, track their impact, and earn rewards. Join us!! Vertical scroll bar, 1 page Horizontal scroll bar, 1 page"])[20]/XCUIElementTypeOther[4]/XCUIElementTypeOther',
            "i_onboarding_get_started": '(//XCUIElementTypeOther[@name="Continue with Email."])[2]',
            "i_onboarding_get_started_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView',
            "i_sign_up_with_email_btn": '(//XCUIElementTypeOther[@name="Continue with Email."])[2]',
            "i_sign_up_with_email_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView',
            "i_sign_up_with_email_emailsvgicon": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView',
            "i_text_btn": "Continue with Email.",
            "i_sign_up_with_google_btn": '/hierarchy/android.widnget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]',
            "i_sign_up_with_google_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView',
            "i_text_sign_up_with_google_btn": 'Continue with Google.',
            "i_signup_title": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView',
            "i_input_email_address": '(//XCUIElementTypeOther[@name="Email"])[2]/XCUIElementTypeTextField',
            "i_input_first_name": '(//XCUIElementTypeOther[@name="First Name"])[2]/XCUIElementTypeTextField',
            "i_input_last_name": '(//XCUIElementTypeOther[@name="Last Name"])[2]/XCUIElementTypeTextField',
            "i_input_password": '//XCUIElementTypeOther[@name="Enter password"]/XCUIElementTypeSecureTextField',
            "i_retype_password": '//XCUIElementTypeOther[@name="Confirm Password"]/XCUIElementTypeSecureTextField',
            "i_sign_up_btn": '//XCUIElementTypeOther[@name="Sign Up"]',
            "i_notif_allow_link": '//XCUIElementTypeButton[@name="Allow"]',
            "i_id_notif_allow_link": 'com.android.permissioncontroller:id/permission_allow_button',
            "i_sprout_tooltip_txt": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView',
            "i_sprout_tooltip": '(//XCUIElementTypeOther[@name="Next"])[2]',
            "i_compost_tooltip": '(//XCUIElementTypeOther[@name="Next Tooltip c"])[2]',
            "i_ewaste_tooltip": '(//XCUIElementTypeOther[@name="Next"])[2]',
            "i_lower_energy_tooltip": '(//XCUIElementTypeOther[@name="Done"])[2]'

        }

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver
        run_em = RandomEmailGenerator()
        run_em.generate_random_email()
        print(f"onboarding: {CommonCache.email}")

    def find_element(self, element_name):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_map[element_name])))

    def Get_started(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("iOS_allow_popup").click()
                get = self.find_element("i_get_started_btn")
                get.click()
                print(get)
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("get_started_btn").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("get_started_btn element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def Onboarding_arrow_1(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_onboarding_arrow_1").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("onboarding_arrow_1").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("onboarding_arrow_1 element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def Onboarding_arrow_2(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_onboarding_arrow_2").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("onboarding_arrow_2").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("onboarding_arrow_2 element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def Onboarding_arrow_3(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_onboarding_arrow_3").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("onboarding_arrow_3").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("onboarding_arrow_3 element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def sign_up_with_email(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("sign_up_with_email_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("sign_up_with_email_btn").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("sign_up_with_email_btn element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def input_email(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_input_email_address").send_keys(CommonCache.email)
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("input_email_address").send_keys(CommonCache.email)
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("input_email_address element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def input_fname(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_input_first_name").send_keys("john")
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("input_first_name").send_keys("William")
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("input_first_name element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def input_lname(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_input_last_name").send_keys("jack")
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("input_last_name").send_keys("jack")
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("input_last_name element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def input_password(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_input_password").send_keys("P@ss1234")
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("input_password").send_keys("P@ss1234")
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("Login link element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def input_retype_password(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_retype_password").send_keys("P@ss1234")
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("retype_password").send_keys("P@ss1234")
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("retype_password element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def sign_up_btn(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_sign_up_btn").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("sign_up_btn").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("sign_up_btn element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def notif_allow_link(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_notif_allow_link").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("notif_allow_link").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("notif_allow_link element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def sprout_tooltip(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_sprout_tooltip").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("sprout_tooltip").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("sprout_tooltip element not found for any platform.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def compost_tooltip(self):
        try:
            # Check for iOS specific elements
            if self.is_ios():
                self.find_element("i_compost_tooltip").click()
                return True

            # Check for Android specific elements
            elif self.is_android():
                self.find_element("compost_tooltip").click()
                return True
            # If neither iOS nor Android elements are found, raise an exception
            else:
                raise Exception("compost_tooltip element not found for any platform.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def is_ios(self):
        platform_name = self.driver.capabilities['platformName']
        return platform_name.lower() == 'ios'

    def is_android(self):
        platform_name = self.driver.capabilities['platformName']
        return platform_name.lower() == 'android'

# if __name__ == "__main__":
#     pytest.main()
#     run = OnboardingPage()
#     run.Get_started()
#     run.Onboarding_arrow_1()
#     run.sign_up_with_email()
#     run.input_email()
# run.input_fname()
# run.input_lname()
# run.input_password()
# run.input_retype_password()
# run.sign_up_btn()
