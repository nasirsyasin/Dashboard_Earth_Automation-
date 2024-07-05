from Utility.web_driver_base_setup import web_driver_setup
from selenium import webdriver


def driver_access_mixpanel():
    mixpanel_url = 'https://mixpanel.com/project/3312156/view/3817088/app/events'
    driver = web_driver_setup(mixpanel_url)
    return driver
