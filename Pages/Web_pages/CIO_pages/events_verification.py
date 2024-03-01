import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from CiO_login import test_cio_login
from Utility.web_driver_base_setup import web_driver_setup, loadCookies
from driver_access import driver_access_cio

driver = driver_access_cio()


def test_events_verification():
    loadCookies(driver)
    try:
        time.sleep(10)
        xpath_switch_menu_btn = "#root > div > div > div.hydra-top-nav > div.hydra-top-nav__left-section > div.hydra-top-nav__workspace-selector-container > button"
        menu_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, xpath_switch_menu_btn))
        )
        menu_btn.click()
        time.sleep(10)
        xpath_dropdown_staging_btn = "//section[@class = 'main-nav-workspace-dropdown__workspaces']/ul/li[2]/a[1]"
        staging_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_dropdown_staging_btn))
        )

        staging_btn.click()
        time.sleep(10)
        xpath_activity_log_btn = "#root > div > div > div:nth-child(3) > div.main-nav-container.main-nav-container--has-aside > div > div > div.main-nav__main > div:nth-child(4) > a:nth-child(4) > div.main-nav__main-link-label"
        activity_log_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, xpath_activity_log_btn))
        )

        activity_log_btn.click()
        time.sleep(10)
        xpath_user_log_details_btn = "//a[text()='Zubair Shahid'][1]"
        user_log_details_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_user_log_details_btn))
        )
        user_log_details_btn.click()
        time.sleep(10)
        xpath_more_logs_link = '//header[@aria-labelledby="recent-activity-header"]/a'
        user_log_details_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_more_logs_link))
        )
        user_log_details_btn.click()
        time.sleep(10)
        xpath_cio_events_rows = "//table/tbody"
        event_text = driver.find_element(By.XPATH, xpath_cio_events_rows).text
        given_text = "app_open"
        given_text1 = "tech tiz"

        for char_event in event_text.split():
            print(char_event)
            if given_text in char_event:
                print(given_text)

        #
        # xpath_stage_btn = "//section[@class = 'main-nav-workspace-dropdown__workspaces']/ul/li[2]/a[1]"
        # stage = WebDriverWait(driver, 100).until(
        #     EC.presence_of_element_located((By.XPATH, xpath_stage_btn))
        # )
        # stage.click()
        # time.sleep(10)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    pytest.main()
