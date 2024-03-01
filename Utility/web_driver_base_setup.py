import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
import time

options = Options()


def web_driver_setup(web_url):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(web_url)

    time.sleep(15)

    return driver


def saveCookies(driver):
    # Get and store cookies after login
    cookies = driver.get_cookies()

    # Store cookies in a file
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print('New Cookies saved successfully')


def loadCookies(driver):
    # Check if cookies file exists
    if 'cookies.json' in os.listdir():

        # Load cookies to a variable from a file
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)

        # Set stored cookies to maintain the session
        for cookie in cookies:
            driver.add_cookie(cookie)
    else:
        print('No cookies file found')

    driver.refresh()  # Refresh Browser after login

