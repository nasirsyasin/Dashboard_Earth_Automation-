import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton

# driver initialization
appium_driver_singleton = AppiumDriverSingleton()
appium_driver = appium_driver_singleton.get_driver


class Ewaste_onboarding_locators:
    xpath_ewaste_action_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.View'
    xpath_ewaste_action_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView[2]'
    # xpath_ewaste_yes_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
    xpath_ewaste_yes_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
    xpath_ewaste_no_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
    xpath_ewaste_no_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView'
    xpath_ewaste_not_sure_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'
    xpath_ewaste_not_sure_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView'
    xpath_ewaste_no_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup'
    xpath_ewaste_no_back_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'
    xpath_ewaste_not_sure_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'
    # xpath_ewaste_not_sure_back_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
    # xpath_ewaste_yes_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'
    xpath_ewaste_yes_back_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'


def test_Ewaste_onboarding():
    global ewaste_no_btn_status, ewaste_no_arrow_status, ewaste_action_btn_not_sure_status, ewaste_not_sure_btn_status
    wait = WebDriverWait(appium_driver, 200)
    time.sleep(10)
    ewaste_action_btn = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   Ewaste_onboarding_locators.xpath_ewaste_action_txt)))
    if ewaste_action_btn.is_displayed():
        ewaste_action_btn.click()
        ewaste_action_btn_status = True
        ewaste_no_btn = wait.until(
            EC.presence_of_element_located((By.XPATH, Ewaste_onboarding_locators.xpath_ewaste_no_btn)))
        if ewaste_no_btn.is_displayed():
            ewaste_no_btn.click()
            ewaste_no_btn_status = True
            ewaste_no_arrow = wait.until(
                EC.presence_of_element_located((By.XPATH, Ewaste_onboarding_locators.xpath_ewaste_no_arrow)))
            if ewaste_no_arrow.is_displayed():
                ewaste_no_arrow.click()
                ewaste_no_arrow_status = True
                time.sleep(10)
                ewaste_action_btn_not_sure = wait.until(
                    EC.presence_of_element_located((By.XPATH, Ewaste_onboarding_locators.xpath_ewaste_action_btn)))
                if ewaste_action_btn_not_sure.is_displayed():
                    ewaste_action_btn_not_sure.click()
                    ewaste_action_btn_not_sure_status = True
                    ewaste_not_sure_btn = wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, Ewaste_onboarding_locators.xpath_ewaste_not_sure_btn)))
                    if ewaste_not_sure_btn.is_displayed():
                        ewaste_not_sure_btn.click()
                        ewaste_not_sure_btn_status = True

                    else:
                        ewaste_not_sure_btn_status = False

                else:
                    ewaste_action_btn_not_sure_status = False

            else:
                ewaste_no_arrow_status = False
        else:
            ewaste_no_btn_status = False
    else:
        ewaste_action_btn_status = False

    return (ewaste_action_btn_status, ewaste_no_btn_status, ewaste_no_arrow_status, ewaste_action_btn_not_sure_status,
            ewaste_not_sure_btn_status)


class Ewaste_complete_locators:
    xpath_ewaste_not_sure_back_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
    xpath_ewaste_yes_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
    xpath_ewaste_yes_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'
    xpath_ewaste_map_link = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
    xpath_ewaste_photo_upload_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
    xpath_ewaste_map_details_cross = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
    xpath_ewaste_camera_btn = '//android.widget.Button[@content-desc="Camera"]'
    xpath_ewaste_camera_permission = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'
    xpath_ewaste_camera_capture = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]'
    xpath_save_ok_photo = '//android.widget.Button[@content-desc="OK"]/android.view.ViewGroup/android.widget.TextView'
    xpath_verify_complete_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'
    xpath_completed_action_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'


def test_yes_flow():
    global ewaste_yes_btn_status, ewaste_yes_arrow_status
    wait = WebDriverWait(appium_driver, 200)
    time.sleep(10)
    ewaste_not_sure_back_arrow = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, Ewaste_complete_locators.xpath_ewaste_not_sure_back_arrow)))
    if ewaste_not_sure_back_arrow.is_displayed():
        ewaste_not_sure_back_arrow.click()
        ewaste_not_sure_back_arrow_status = True
        ewaste_yes_btn = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, Ewaste_complete_locators.xpath_ewaste_yes_btn)))
        if ewaste_yes_btn.is_displayed():
            ewaste_yes_btn.click()
            ewaste_yes_btn_status = True
            ewaste_yes_arrow = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, Ewaste_complete_locators.xpath_ewaste_yes_arrow)))
            if ewaste_yes_arrow.is_displayed():
                ewaste_yes_arrow.click()
                ewaste_yes_arrow_status = True

            else:
                ewaste_yes_arrow_status = False

        else:
            ewaste_yes_btn_status = False

    else:
        ewaste_not_sure_back_arrow_status = False
    return ewaste_not_sure_back_arrow_status, ewaste_yes_btn_status, ewaste_yes_arrow_status


def test_map_photo_upload():
    wait = WebDriverWait(appium_driver, 200)
    time.sleep(10)
    ewaste_map_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, Ewaste_complete_locators.xpath_ewaste_map_link)))
    if ewaste_map_link.is_displayed():
        ewaste_map_link.click()
        ewaste_map_link_status = True
        ewaste_map_details_cross = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, Ewaste_complete_locators.xpath_ewaste_map_details_cross)))
        if ewaste_map_details_cross.is_displayed():
            ewaste_map_details_cross.click()
            ewaste_map_details_cross_status = True

            ewaste_photo_cap_btn = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, Ewaste_complete_locators.xpath_ewaste_photo_upload_btn)))
            if ewaste_photo_cap_btn.is_displayed():
                ewaste_photo_cap_btn.click()
                ewaste_photo_cap_btn_status = True

                ewaste_camera_btn = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, Ewaste_complete_locators.xpath_ewaste_camera_btn)))
                if ewaste_camera_btn.is_displayed():
                    ewaste_camera_btn.click()
                    ewaste_camera_btn_status = True
                    ewaste_camera_permission = wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, Ewaste_complete_locators.xpath_ewaste_camera_permission)))
                    if ewaste_camera_permission.is_displayed():
                        ewaste_camera_permission.click()
                        ewaste_camera_permission_status = True

                        ewaste_camera_capture = wait.until(
                            EC.presence_of_element_located(
                                (By.XPATH, Ewaste_complete_locators.xpath_ewaste_camera_capture)))
                        if ewaste_camera_capture.is_displayed():
                            ewaste_camera_capture.click()
                            ewaste_camera_capture_status = True

                            save_ok_photo = wait.until(
                                EC.presence_of_element_located(
                                    (By.XPATH, Ewaste_complete_locators.xpath_save_ok_photo)))
                            if save_ok_photo.is_displayed():
                                save_ok_photo.click()
                                save_ok_photo_status = True

                                verify_complete_btn = wait.until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, Ewaste_complete_locators.xpath_verify_complete_btn)))
                                if verify_complete_btn.is_displayed():
                                    verify_complete_btn.click()
                                    verify_complete_btn_status = True
                                    completed_action_btn = wait.until(
                                        EC.presence_of_element_located(
                                            (By.XPATH, Ewaste_complete_locators.xpath_completed_action_btn)))
                                    if completed_action_btn.is_displayed():
                                        completed_action_btn.click()
                                        completed_action_btn_status = True

                                    else:
                                        completed_action_btn_status = False

                                else:
                                    verify_complete_btn_status = False

                            else:
                                save_ok_photo_status = False

                        else:
                            ewaste_camera_capture_status = False

                    else:
                        ewaste_camera_permission_status = False

                else:
                    ewaste_camera_btn_status = False

            else:
                ewaste_photo_cap_btn_status = False

        else:
            ewaste_map_details_cross_status = False

    else:
        ewaste_map_link_status = False


if __name__ == "__main__":
    pytest.main()
    pytest.test_Ewaste_onboarding()
    pytest.test_ewaste_complete()
