from Utility.web_driver_base_setup import web_driver_setup, loadCookies


def driver_access_cio():
    wb_cio = 'https://fly.customer.io/login'
    driver = web_driver_setup(wb_cio)

    return driver
