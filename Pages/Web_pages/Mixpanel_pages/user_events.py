import time

import pytest
from selenium.webdriver.common.by import By
from Pages import driver_access_mixpanel
from Utility.web_driver_base_setup import loadCookies

driver = driver_access_mixpanel()


def test_mixpanel_user_events():
    loadCookies(driver)
    time.sleep(10)
    try:
        shadow_root = driver.find_element(By.XPATH, '//mp-chrome-header').shadow_root
        shadow_text = shadow_root.find_element(By.CSS_SELECTOR,
                                               'div > div > div > div.mp-chrome-header-left > div > a:nth-child(3)')
        shadow_text.click()
        time.sleep(10)
        shadow_root_table = driver.find_element(By.XPATH, '//mp-table').shadow_root
        print(shadow_root_table)
        time.sleep(10)
        # Find all elements with the class name containing email
        email_elements = shadow_root_table.find_elements(By.CSS_SELECTOR, 'div > div.mp-table-body.mp-table-body-clickable.mp-table-body-scroll > div:nth-child(2)')
        email_elements.click()
        time.sleep(10)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    pytest.main()
