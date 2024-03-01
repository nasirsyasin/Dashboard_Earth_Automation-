import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Utility.web_driver_base_setup import web_driver_setup, saveCookies, loadCookies

wb_cio = 'https://fly.customer.io/login'
driver = web_driver_setup(wb_cio)


def test_cio_login():
    loadCookies(driver)
    try:
        xpath_google_sign_in_btn = "//div/button[@type =  'button']"
        google_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_google_sign_in_btn))
        )
        google_btn.click()
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[1])

        xpath_google_sign_in_input = "//div/input[@type= 'email']"
        google_email_input = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_google_sign_in_input))
        )
        google_email_input.click()
        google_email_input.clear()
        google_email_input.send_keys("zubair.shahid@mavrictech.com")
        time.sleep(10)
        xpath_email_next_btn = "//div[@id = 'identifierNext']/div/button"
        google_email_next_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_email_next_btn))
        )
        google_email_next_btn.click()
        time.sleep(10)
        xpath_pwd_input = "//input[@type='password']"
        google_pwd_input = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_pwd_input))
        )
        google_pwd_input.click()
        google_pwd_input.clear()
        google_pwd_input.send_keys("Devigital@321")
        time.sleep(10)
        xpath_pwd_btn = "//div[@id = 'passwordNext']/div/button"
        google_pwd_next_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_pwd_btn))
        )
        google_pwd_next_btn.click()
        time.sleep(10)
        saveCookies(driver)
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    pytest.main()
