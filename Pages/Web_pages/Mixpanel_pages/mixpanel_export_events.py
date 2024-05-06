import csv
from bs4 import BeautifulSoup
import pytest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from mixpanel_web_access import driver_access_mixpanel
from selenium.webdriver.support import expected_conditions as EC
from Utility.web_driver_base_setup import loadCookies

driver = driver_access_mixpanel()
mixpanel_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/mixpanel_events.csv"


def test_mixpanel():
    loadCookies(driver)
    time.sleep(5)
    try:
        time.sleep(5)
        filter_shadow_root = driver.find_element(By.XPATH, '//mp-section[@header-title="Filters"]').shadow_root
        time.sleep(5)

        filter_btn = filter_shadow_root.find_element(By.CSS_SELECTOR,
                                                     'div > div.mp-section-title-container > div.mp-section-actions > mp-button')
        filter_btn.click()

        # time.sleep(5)
        # add_filter_shadow_root = driver.find_element(By.XPATH,
        #                                              '//mp-query-entry-section[@elref="filterSection"]').shadow_root
        # print(add_filter_shadow_root)

        time.sleep(5)
        # add_filter_btn = add_filter_shadow_root.find_element(By.CSS_SELECTOR,
        # 'div > div.mp-query-entry-section-footer.is-empty > div > div > mp-button')
        add_filter_btn = driver.find_element(By.XPATH, '//div[@elref="filterSection"]/div/div/div/mp-button['
                                                       '@class="new-entry-button"]')

        # add_filter_btn = driver.execute_script(
        #     "return document.querySelector('#mixpanel-application > inspector-app > mp-sidenav-layout > "
        #     "div.inspector-app-query-builder-container > mp-query-builder-xzmlyo > div > div > div > mp-section > div "
        #     "> div > div > div.mp-query-entry-section-footer.is-empty > div > div > mp-button')"
        # )
        add_filter_btn.click()

        time.sleep(5)
        # Execute JavaScript to find the username field
        # search_email = driver.execute_script(
        #     "return document.querySelector('#mixpanel-application > inspector-app > mp-sidenav-layout > "
        #     "div.inspector-app-query-builder-container > mp-query-builder-xzmlyo > div > div > div > mp-section > div "
        #     "> div > div > div.mp-query-entry-section-body > div > div.mp-query-entry-body > div > div:nth-child(1) > "
        #     "div > div.mp-query-block-selector.mp-query-editing > div.mp-query-drop-menu-container.for-filter-menu > "
        #     "mp-drop-menu > div > div > div > div > div.search-wrapper > mp-input').shadowRoot.querySelector('div > "
        #     "div > div.mp-input-wrapper > input')"
        # )
        search_email = driver.find_element(By.XPATH, '//mp-input[@elref="searchInput"]')
        search_email.send_keys("Email")

        # Set value for the search field
        # driver.execute_script("arguments[0].setAttribute('value', 'email')", search_email)
        time.sleep(5)

        # Execute JavaScript to find the email field
        # email_filter = driver.execute_script(
        #     "return document.querySelector('#mixpanel-application > inspector-app > mp-sidenav-layout > "
        #     "div.inspector-app-query-builder-container > mp-query-builder-xzmlyo > div > div > div > mp-section > div "
        #     "> div > div > div.mp-query-entry-section-body > div > div.mp-query-entry-body > div > div:nth-child(1) > "
        #     "div > div.mp-query-block-selector.mp-query-editing > div.mp-query-drop-menu-container.for-filter-menu > "
        #     "mp-drop-menu > div > div > div > div > div.mp-properties-menu-wrapper > div > "
        #     "mp-items-menu').shadowRoot.querySelector('div > div > div:nth-child(1) > ul > div:nth-child(1) > li > "
        #     "div.option-label-section.sublabel-theme-breadcrumb.has-sublabel > div > div > span.label')"
        # )
        # driver.execute_script("arguments[0].click()", event_filter)
        email_filter_shadow_root = driver.find_element(By.XPATH,
                                                       '//mp-items-menu[@elref="mainSelectionMenu"]').shadow_root
        email_filter = email_filter_shadow_root.find_element(By.CSS_SELECTOR,
                                                             'div > div > div:nth-child(1) > ul > div:nth-child(1) > li > div.option-label-section.sublabel-theme-breadcrumb.has-sublabel > div > div > span.label')
        email_filter.click()
        time.sleep(5)

        # element = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR,
        #                                       '#mixpanel-application > inspector-app > mp-sidenav-layout > div.inspector-app-query-builder-container > mp-query-builder-t0sarg > div > div > div > mp-section > div > div > div > div.mp-query-entry-section-body > div > div.mp-query-entry-body > div > div.mp-query-entry-filter-parts > div > mp-select.filter-value-select.is-placeholder.is-open > mp-property-values-screen'))
        # )

        # enter_email_filter = driver.execute_script(
        #     'return document.querySelector("#mixpanel-application > inspector-app > mp-sidenav-layout > '
        #     'div.inspector-app-query-builder-container > mp-query-builder-xzmlyo > div > div > div > mp-section > div '
        #     '> div > div > div.mp-query-entry-section-body > div > div.mp-query-entry-body > div > '
        #     'div.mp-query-entry-filter-parts > div > mp-select.filter-value-select.is-open > '
        #     'mp-property-values-screen").shadowRoot.querySelector("div > div > div.pvs-filter-fixed-subsection > '
        #     'mp-input").shadowRoot.querySelector("div > div > div.mp-input-wrapper > input")'
        # )

        filter_shadow_r = driver.find_element(By.XPATH, '//mp-property-values-screen[@elref="filterValue"]').shadow_root
        element_within_first_shadow_root = filter_shadow_r.find_element(By.CSS_SELECTOR,
                                                                        'div > div > div.pvs-filter-fixed-subsection > mp-input')
        second_shadow_root = element_within_first_shadow_root.shadow_root
        enter_email_filter = second_shadow_root.find_element(By.CSS_SELECTOR,
                                                             'div > div > div.mp-input-wrapper > input')

        enter_email_filter.send_keys('zubair.shahid+473938@mavrictech.com')
        time.sleep(10)

        element2_within_first_shadow_root = filter_shadow_r.find_element(By.CSS_SELECTOR,
                                                                         'div > div > div.pvs-filter-property-values > mp-items-menu')
        second2_shadow_root = element2_within_first_shadow_root.shadow_root
        select_email_filter = second2_shadow_root.find_element(By.CSS_SELECTOR,
                                                               'div > div > div:nth-child(3) > ul > div > li > mp-checkbox')

        select_email_filter.click()
        # select_email_filter = driver.execute_script(
        #     "return document.querySelector('#mixpanel-application > inspector-app > mp-sidenav-layout > "
        #     "div.inspector-app-query-builder-container > mp-query-builder > div > div > mp-section > div > "
        #     "mp-query-entry-section').shadowRoot.querySelector('div > div.mp-query-entry-section-body > div > "
        #     "div.mp-query-entry-body > div > div.mp-query-entry-filter-parts > div > mp-select.is-placeholder.is-open "
        #     "> mp-property-values-screen').shadowRoot.querySelector('div > div > div.pvs-filter-property-values > "
        #     "mp-items-menu').shadowRoot.querySelector('div > div > div:nth-child(3) > ul > div')"
        # )
        # # driver.execute_script("arguments[0].click()", event_filter)
        # select_email_filter.click()
        time.sleep(5)
        # add_email_filter = driver.execute_script(
        #     "return document.querySelector('#mixpanel-application > inspector-app > mp-sidenav-layout > "
        #     "div.inspector-app-query-builder-container > mp-query-builder > div > div > mp-section > div > "
        #     "mp-query-entry-section').shadowRoot.querySelector('div > div.mp-query-entry-section-body > div > "
        #     "div.mp-query-entry-body > div > div.mp-query-entry-filter-parts > div > mp-select.is-placeholder.is-open "
        #     "> mp-property-values-screen').shadowRoot.querySelector('div > mp-button-bar').shadowRoot.querySelector("
        #     "'div')"
        # )
        # driver.execute_script("arguments[0].click()", event_filter)
        add_email_filter_shadow_r = driver.find_element(By.XPATH,
                                                        '//mp-property-values-screen[@elref="filterValue"]').shadow_root
        add_email_filter = add_email_filter_shadow_r.find_element(By.CSS_SELECTOR,
                                                                  'div > mp-button-bar')
        add_email_filter.click()
        time.sleep(5)

        shadow_root_mp_table = driver.find_element(By.XPATH, '//mp-table').shadow_root

        # Assuming you have initialized your webdriver and obtained the shadow_root

        table_html = shadow_root_mp_table.find_element(By.CSS_SELECTOR, "div.mp-table").get_attribute('innerHTML')

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(table_html, 'html.parser')

        # Find all table rows
        rows = soup.find_all('div', class_='mp-table-row')

        # Set to store unique data
        unique_data = set()

        # Writing to CSV
        with open(mixpanel_events, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Write header row
            csvwriter.writerow(['Event Name'])

            # Write data rows
            for row in rows:
                # Extracting data from HTML row
                event_name = row.find('div', class_='cell-event-name').get_text(strip=True)

                # Creating a unique key for each row
                data_key = event_name

                # Check if the data is unique before writing to CSV
                if data_key not in unique_data:
                    unique_data.add(data_key)
                    csvwriter.writerow([
                        event_name
                    ])

        time.sleep(10)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    pytest.main()
    pytest.test_mixpanel()
