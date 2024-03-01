import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utility.mobile_driver_setup import AppiumDriverSingleton

# driver initialization
appium_driver_singleton = AppiumDriverSingleton()
appium_driver = appium_driver_singleton.get_driver


class LoginScreen:
    xpath_login_link = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView'
    xpath_welcome_screen_back_icon = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView'
    xpath_email_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]'
    xpath_password_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]'
    xpath_login_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[8]'
    xpath_test = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout'


def Login_Screen():
    global login_email_input_status, login_password_input_status, login_btn_status, test_case_status
    wait = WebDriverWait(appium_driver, 100)
    login_link = wait.until(EC.presence_of_element_located((By.XPATH, LoginScreen.xpath_login_link)))
    if login_link.is_displayed():

        login_link.click()
        print('Login link button is clicked')
        login_link_status = True
        login_email_input = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       LoginScreen.xpath_email_input)))
        if login_email_input.is_displayed():
            login_email_input.clear()
            login_email_input.send_keys("zubair.shahid+61976@mavrictech.com")
            login_email_input_status = True
            login_password_input = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                              LoginScreen.xpath_password_input)))
            if login_password_input.is_displayed():
                login_password_input.clear()
                login_password_input.send_keys("P@ss1234")
                login_password_input_status = True
                login_btn = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       LoginScreen.xpath_login_btn)))
                if login_btn.is_displayed():
                    login_btn.click()
                    login_btn_status = True
                    test_case = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                           LoginScreen.xpath_test)))

                    if test_case.is_displayed():
                        test_case.click()
                        test_case_status = True
                    else:
                        test_case_status = False
                else:
                    login_btn_status = False
            else:
                login_password_input_status = False
        else:
            login_email_input_status = False
    else:
        login_link_status = False

    return login_link_status, login_email_input_status, login_password_input_status, login_btn_status, test_case_status


if __name__ == "__main__":
    pytest.main()
