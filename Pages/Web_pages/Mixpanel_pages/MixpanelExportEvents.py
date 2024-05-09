import csv
import time

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from Pages.Web_pages.mixpanel_web_access import driver_access_mixpanel
from Utility.web_driver_base_setup import loadCookies


class MixpanelExportEvents:
    def __init__(self):
        self.driver = driver_access_mixpanel()
        self.mixpanel_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/mixpanel_events.csv"

    def export_events(self):
        loadCookies(self.driver)
        time.sleep(5)
        try:
            time.sleep(5)
            filter_shadow_root = self.driver.find_element(By.XPATH, '//mp-section[@header-title="Filters"]').shadow_root
            time.sleep(5)

            filter_btn = filter_shadow_root.find_element(By.CSS_SELECTOR,
                                                         'div > div.mp-section-title-container > div.mp-section-actions > mp-button')
            filter_btn.click()

            time.sleep(5)
            add_filter_btn = self.driver.find_element(By.XPATH, '//div[@elref="filterSection"]/div/div/div/mp-button['
                                                                '@class="new-entry-button"]')
            add_filter_btn.click()

            time.sleep(5)
            search_email = self.driver.find_element(By.XPATH, '//mp-input[@elref="searchInput"]')
            search_email.send_keys("Email")

            time.sleep(5)
            email_filter_shadow_root = self.driver.find_element(By.XPATH,
                                                                '//mp-items-menu[@elref="mainSelectionMenu"]').shadow_root
            email_filter = email_filter_shadow_root.find_element(By.CSS_SELECTOR,
                                                                 'div > div > div:nth-child(1) > ul > div:nth-child(1) > li > div.option-label-section.sublabel-theme-breadcrumb.has-sublabel > div > div > span.label')
            email_filter.click()
            time.sleep(5)

            filter_shadow_r = self.driver.find_element(By.XPATH,
                                                       '//mp-property-values-screen[@elref="filterValue"]').shadow_root
            element_within_first_shadow_root = filter_shadow_r.find_element(By.CSS_SELECTOR,
                                                                            'div > div > div.pvs-filter-fixed-subsection > mp-input')
            second_shadow_root = element_within_first_shadow_root.shadow_root
            enter_email_filter = second_shadow_root.find_element(By.CSS_SELECTOR,
                                                                 'div > div > div.mp-input-wrapper > input')

            enter_email_filter.send_keys('zubair.shahid+1200073@mavrictech.com')
            time.sleep(10)

            filter_select_shadow_r = self.driver.find_element(By.XPATH,
                                                              '//mp-property-values-screen[@elref="filterValue"]').shadow_root
            element2_within_first_shadow_root = filter_select_shadow_r.find_element(By.CSS_SELECTOR,
                                                                                    'div > div > div.pvs-filter-property-values > mp-items-menu')
            second2_shadow_root = element2_within_first_shadow_root.shadow_root
            select_email_filter = second2_shadow_root.find_element(By.CSS_SELECTOR,
                                                                   'div > div > div:nth-child(3) > ul > div > li > mp-checkbox')

            select_email_filter.click()
            time.sleep(5)

            add_email_filter_shadow_r = self.driver.find_element(By.XPATH,
                                                                 '//mp-property-values-screen[@elref="filterValue"]').shadow_root
            add_email_filter = add_email_filter_shadow_r.find_element(By.CSS_SELECTOR,
                                                                      'div > mp-button-bar')
            add_email_filter.click()
            time.sleep(5)

            shadow_root_mp_table = self.driver.find_element(By.XPATH, '//mp-table').shadow_root

            table_html = shadow_root_mp_table.find_element(By.CSS_SELECTOR, "div.mp-table").get_attribute('innerHTML')

            soup = BeautifulSoup(table_html, 'html.parser')

            rows = soup.find_all('div', class_='mp-table-row')

            unique_data = set()

            with open(self.mixpanel_events, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['Event Name'])
                for row in rows:
                    event_name = row.find('div', class_='cell-event-name').get_text(strip=True)
                    data_key = event_name
                    if data_key not in unique_data:
                        unique_data.add(data_key)
                        csvwriter.writerow([event_name])

            time.sleep(10)

        except Exception as e:
            print(f"Exception: {e}")
