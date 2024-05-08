from Utility.web_driver_base_setup import web_driver_setup
from selenium import webdriver


def driver_access_mixpanel():
    mixpanel_url = 'https://mixpanel.com/project/2462599/view/3005471/app/events'
    driver = web_driver_setup(mixpanel_url)
    return driver
