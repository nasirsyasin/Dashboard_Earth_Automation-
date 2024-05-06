import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utility.web_driver_base_setup import loadCookies, saveCookies
from Pages.Web_pages.Mixpanel_pages.mixpanel_web_access import driver_access_mixpanel

driver = driver_access_mixpanel()


def test_login_to_mixpanel():
    loadCookies(driver)
    try:
        login_btn_xpath = "//button/div[contains(., 'Login')]"
        login_link_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, login_btn_xpath))
        )
        # print("Parent window title: " + driver.title)
        login_link_btn.click()
        time.sleep(5)
        # Switch to the iframe using its relative XPath
        iframe_xpath = '//div[@class="g_id_signin"]/div/iframe'
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, iframe_xpath))
        )
        # print("iframe : " + iframe)
        driver.switch_to.frame(iframe)
        # Wait for the "Sign in with Google" button to be present on the page
        google_btn_xpath = "//div[@id='container']/div/div[2]"
        google_btn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, google_btn_xpath))
        )
        # print("Parent window title: " + driver.title)
        google_btn.click()
        time.sleep(5)

        driver.switch_to.window(driver.window_handles[1])

        xpath_email_input = "//div/input[@type = 'email']"
        email_input = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_email_input))
        )
        email_input.click()
        email_input.clear()
        email_input.send_keys("zubair.shahid@mavrictech.com")

        xpath_Next_button = "//div[@id = 'identifierNext']/div/button"
        next_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_Next_button))
        )
        next_btn.click()

        time.sleep(10)
        xpath_password_input = "//input[@type='password']"
        password_input = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_password_input))
        )
        password_input.click()
        password_input.clear()
        password_input.send_keys("Devigital@321")

        time.sleep(10)

        xpath_passwordNext_button = "//div[@id = 'passwordNext']/div/button"
        password_next_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath_passwordNext_button))
        )
        password_next_btn.click()
        time.sleep(10)

        # Switch back to the default content
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(10)
        saveCookies(driver)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    pytest.main()
