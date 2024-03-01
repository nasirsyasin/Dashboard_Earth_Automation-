import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.random_email_generator import random_email_gen
from Utility.mobile_driver_setup import AppiumDriverSingleton
import time

# driver initialization
appium_driver_singleton = AppiumDriverSingleton()
appium_driver = appium_driver_singleton.get_driver

# random email
random_email = random_email_gen()


class SplashScreen:
    xpath_get_started_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'
    # xpath_login_link = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView'
    xpath_non_la_sc_back_icon = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
    xpath_non_la_link = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView'
    # ElementID
    text_explore_other_cl_actions = 'EXPLORE OTHER CLIMATE ACTIONS'


def EntryScreen():
    wait = WebDriverWait(appium_driver, 100)
    get_started_btn = wait.until(EC.presence_of_element_located((By.XPATH, SplashScreen.xpath_get_started_btn)))
    if get_started_btn.is_displayed():
        get_started_btn.click()
        get_started_btn_status = True
    else:
        get_started_btn_status = False

    return get_started_btn_status


class onboarding_screens_locators:
    xpath_onboarding_arrow_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/com.horcrux.svg.SvgView'
    xpath_onboarding_arrow_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup'
    xpath_onboarding_arrow_3 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup'
    xpath_onboarding_get_started = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'
    xpath_onboarding_get_started_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'


def onboarding_screens():
    wait = WebDriverWait(appium_driver, 100)

    onboarding_arrow_1 = wait.until(
        EC.presence_of_element_located((By.XPATH, onboarding_screens_locators.xpath_onboarding_arrow_1)))
    if onboarding_arrow_1.is_displayed():
        onboarding_arrow_1.click()
        onboarding_arrow_1_status = True
    else:
        onboarding_arrow_1_status = False

        time.sleep(10)

    # onboarding_arrow_2 = wait.until(
    #         EC.presence_of_element_located((By.XPATH, onboarding_screens_locators.xpath_onboarding_arrow_2)))

    x_coordinate = 903, 2194
    y_coordinate = 959, 2242
    onboarding_arrow_2 = [x_coordinate, y_coordinate]
    time.sleep(10)

    if onboarding_arrow_2:
        # onboarding_arrow_2.click()
        appium_driver.tap(onboarding_arrow_2)
        onboarding_arrow_2_status = True

    else:
        onboarding_arrow_2_status = False

    time.sleep(10)

    onboarding_arrow_3 = wait.until(
        EC.presence_of_element_located((By.XPATH, onboarding_screens_locators.xpath_onboarding_arrow_3)))

    # x_coordinate1 = 1130, 2740
    # y_coordinate2 = 1354, 2900
    # onboarding_arrow_3 = [x_coordinate1, y_coordinate2]
    time.sleep(10)

    if onboarding_arrow_3.is_displayed():
        onboarding_arrow_3.click()
        # appium_driver.tap(onboarding_arrow_3)

        onboarding_arrow_3_status = True

    else:
        onboarding_arrow_3_status = False

    time.sleep(10)

    onboarding_get_started_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, onboarding_screens_locators.xpath_onboarding_get_started_txt)))

    time.sleep(10)

    if onboarding_get_started_btn.is_displayed():
        onboarding_get_started_btn.click()

        onboarding_get_started_btn_status = True

    else:
        onboarding_get_started_btn_status = False

    return onboarding_arrow_1_status, onboarding_arrow_2_status, onboarding_arrow_3_status, onboarding_get_started_btn_status


class SocialSignupScreen:
    xpath_sign_up_with_email_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'
    xpath_sign_up_with_email_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView'
    xpath_sign_up_with_email_emailsvgicon = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
    text_btn = "Continue with Email."
    xpath_sign_up_with_google_btn = '/hierarchy/android.widnget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
    xpath_sign_up_with_google_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView'
    text_sign_up_with_google_btn = 'Continue with Google.'


def Social_SignupScreen():
    wait = WebDriverWait(appium_driver, 100)
    sign_up_with_email_btn = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                        SocialSignupScreen.xpath_sign_up_with_email_txt)))
    if sign_up_with_email_btn.is_displayed():
        sign_up_with_email_btn.click()
        sign_up_with_email_btn_status = True
    else:
        sign_up_with_email_btn_status = False
    return sign_up_with_email_btn_status


class SignupEmailScreen:
    xpath_signup_title = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView'
    xpath_input_email_address = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]'
    xpath_input_first_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]'
    xpath_input_last_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[3]'
    xpath_input_password = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[4]'
    xpath_retype_password = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[5]'
    xpath_sign_up_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
    xpath_notif_allow_link = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'
    id_notif_allow_link = 'com.android.permissioncontroller:id/permission_allow_button'
    xpath_sprout_tooltip_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView'
    xpath_sprout_tooltip = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup'
    xpath_compost_tooltip = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
    xpath_ewaste_tooltip = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'


def Signup_EmailScreen():
    wait = WebDriverWait(appium_driver, 100)
    input_email_address = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     SignupEmailScreen.xpath_input_email_address)))
    if input_email_address.is_displayed():
        input_email_address.clear()
        input_email_address.send_keys(random_email)
        email_input_status = True
    else:
        email_input_status = False

    input_fname = wait.until(EC.presence_of_element_located((By.XPATH,
                                                             SignupEmailScreen.xpath_input_first_name)))
    if input_fname.is_displayed():
        input_fname.clear()
        input_fname.send_keys("zampa")
        first_name_input_status = True
    else:
        first_name_input_status = False

    input_lname = wait.until(EC.presence_of_element_located((By.XPATH,
                                                             SignupEmailScreen.xpath_input_last_name)))

    if input_lname.is_displayed():
        input_lname.clear()
        input_lname.send_keys("david")
        last_name_input_status = True
    else:
        last_name_input_status = False

    input_password = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                SignupEmailScreen.xpath_input_password)))

    if input_password.is_displayed():
        input_password.clear()
        input_password.send_keys("P@ss1234")
        password_input_status = True
    else:
        password_input_status = False

    input_retype_password = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       SignupEmailScreen.xpath_retype_password)))

    if input_retype_password.is_displayed():
        input_retype_password.clear()
        input_retype_password.send_keys("P@ss1234")
        retype_password_status = True
    else:
        retype_password_status = False

    sign_up_btn = wait.until(EC.presence_of_element_located((By.XPATH,
                                                             SignupEmailScreen.xpath_sign_up_btn)))

    if sign_up_btn.is_displayed():
        sign_up_btn.click()
        signup_button_status = True
    else:
        signup_button_status = False

    notif_allow_link = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                  SignupEmailScreen.xpath_notif_allow_link)))

    if notif_allow_link.is_displayed():
        notif_allow_link.click()
        notif_allow_link_status = True
    else:
        notif_allow_link_status = False

    sprout_tooltip = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                SignupEmailScreen.xpath_sprout_tooltip)))

    if sprout_tooltip.is_displayed():
        sprout_tooltip.click()
        sprout_tooltip_status = True
    else:
        sprout_tooltip_status = False

    compost_tooltip = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                 SignupEmailScreen.xpath_compost_tooltip)))

    if compost_tooltip.is_displayed():
        compost_tooltip.click()
        compost_tooltip_status = True
    else:
        compost_tooltip_status = False

    ewaste_tooltip = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                SignupEmailScreen.xpath_ewaste_tooltip)))

    if ewaste_tooltip.is_displayed():
        ewaste_tooltip.click()
        ewaste_tooltip_status = True
    else:
        ewaste_tooltip_status = False

    return (email_input_status, first_name_input_status, last_name_input_status, password_input_status,
            retype_password_status, signup_button_status)


if __name__ == "__main__":
    pytest.main()
