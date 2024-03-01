import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton
import time

appium_driver_singleton = AppiumDriverSingleton()
appium_driver = appium_driver_singleton.get_driver


class compost_mvp_locators:
    xpath_sprout_tooltip = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup'
    xpath_sprout_tooltip_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView'
    xpath_compost_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View'
    xpath_get_started_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
    xpath_get_started_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView'
    xpath_explore_climate_link = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'
    xpath_explore_climate_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView'
    xpath_fork_1_yes_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
    xpath_fork_1_yes_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
    xpath_fork_2_yes_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView'
    xpath_fork_3_yes_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView'
    xpath_back_arrow_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'
    xpath_back_arrow_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'


def test_compost_mvp_flow():
    global fork_1_yes_btn_status, fork_2_yes_arrow_status, fork_back_arrow_1_status, fork_back_arrow_2_status
    wait = WebDriverWait(appium_driver, 200)

    mvp_compost_btn = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                 compost_mvp_locators.xpath_compost_btn)))
    if mvp_compost_btn.is_displayed():
        mvp_compost_btn.click()
        mvp_get_started_btn_status = True
        time.sleep(3)

        fork_1_yes_btn = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                    compost_mvp_locators.xpath_fork_1_yes_btn)))
        if fork_1_yes_btn.is_displayed():
            fork_1_yes_btn.click()
            fork_1_yes_btn_status = True
            time.sleep(3)

            fork_2_yes_arrow = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                          compost_mvp_locators.xpath_fork_2_yes_arrow)))

            if fork_2_yes_arrow.is_displayed():
                fork_2_yes_arrow.click()
                fork_2_yes_arrow_status = True
                time.sleep(3)
                fork_back_arrow_1 = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                               compost_mvp_locators.xpath_back_arrow_1)))

                if fork_back_arrow_1.is_displayed():
                    fork_back_arrow_1.click()
                    fork_back_arrow_1_status = True
                    time.sleep(3)
                    fork_back_arrow_2 = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                   compost_mvp_locators.xpath_back_arrow_2)))

                    if fork_back_arrow_2.is_displayed():
                        fork_back_arrow_2.click()
                        fork_back_arrow_2_status = True
                    else:
                        fork_back_arrow_2_status = False
                else:
                    fork_back_arrow_1_status = False
            else:
                fork_2_yes_arrow_status = False
        else:
            fork_1_yes_btn_status = False
    else:
        mvp_get_started_btn_status = False

    return (mvp_get_started_btn_status, fork_1_yes_btn_status, fork_2_yes_arrow_status, fork_back_arrow_1_status,
            fork_back_arrow_2_status)


class compost_mvp_no_locators:
    xpath_fork_1_no_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
    xpath_fork_2_no_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView'
    xpath_fork_3_no_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView'
    xpath_fork_4_no_dropdown = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
    xpath_fork_4_no_arrow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView'


def test_compost_mvp_no_flow():
    global fork_2_no_arrow_status, fork_3_no_arrow_status, fork_4_no_dropdown_status, fork_4_no_dropdown_2_status, fork_4_no_arrow_status
    wait = WebDriverWait(appium_driver, 200)
    time.sleep(3)
    fork_1_no_btn = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               compost_mvp_no_locators.xpath_fork_1_no_btn)))

    if fork_1_no_btn.is_displayed():
        fork_1_no_btn.click()
        fork_1_no_btn_status = True
        time.sleep(3)
        fork_2_no_arrow = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     compost_mvp_no_locators.xpath_fork_2_no_arrow)))
        if fork_2_no_arrow.is_displayed():
            fork_2_no_arrow.click()
            fork_2_no_arrow_status = True
            time.sleep(5)
            fork_3_no_arrow = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                         compost_mvp_no_locators.xpath_fork_3_no_arrow)))
            if fork_3_no_arrow.is_displayed():
                fork_3_no_arrow.click()
                fork_3_no_arrow_status = True
                fork_4_no_open_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                     compost_mvp_no_locators.xpath_fork_4_no_dropdown)))
                if fork_4_no_open_dropdown.is_displayed():
                    fork_4_no_open_dropdown.click()
                    fork_4_no_dropdown_status = True
                    time.sleep(5)
                    fork_4_no_closed_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                           compost_mvp_no_locators.xpath_fork_4_no_dropdown)))
                    if fork_4_no_closed_dropdown.is_displayed():
                        fork_4_no_closed_dropdown.click()
                        fork_4_no_dropdown_2_status = True
                        time.sleep(5)
                        fork_4_no_arrow = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                     compost_mvp_no_locators.xpath_fork_4_no_arrow)))

                        if fork_4_no_arrow.is_displayed():
                            fork_4_no_arrow.click()
                            fork_4_no_arrow_status = True

                        else:
                            fork_4_no_arrow_status = False
                    else:
                        fork_4_no_dropdown_2_status = False

                else:
                    fork_4_no_dropdown_status = False
            else:
                fork_3_no_arrow_status = False
        else:
            fork_2_no_arrow_status = False
    else:
        fork_1_no_btn_status = False

    return (fork_1_no_btn_status, fork_2_no_arrow_status, fork_3_no_arrow_status, fork_4_no_dropdown_status,
            fork_4_no_dropdown_2_status, fork_4_no_arrow_status, compost_done_tooltip_status, complete_compost_status)


class complete_compost:
    xpath_compost_action_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View'


def test_compost_complete():
    global complete_compost_status, compost_done_tooltip_status
    wait = WebDriverWait(appium_driver, 200)

    time.sleep(10)
    x_coordinate1 = 440
    y_coordinate2 = 1480
    compost_done_tooltip = [x_coordinate1, y_coordinate2]

    if compost_done_tooltip:
        appium_driver.tap(compost_done_tooltip)

        compost_done_tooltip_status = True
        time.sleep(10)
        complete_compost_action = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                             complete_compost.xpath_compost_action_btn)))

        if complete_compost_action.is_displayed():
            complete_compost_action.click()

            complete_compost_status = True

        else:
            complete_compost_status = False

    else:
        compost_done_tooltip_status = False
    return complete_compost_status, compost_done_tooltip_status


if __name__ == "__main__":
    pytest.main()
