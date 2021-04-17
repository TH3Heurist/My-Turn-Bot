from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path=DRIVER_BIN)

county = input("County Name: ")
zip_code = input("Zip Code: ")
vac_site = input("Desired Vaccine Site Keyword: ")

while True:
    driver.get('https://myturn.ca.gov/')

    time.sleep(1.5)

    driver.find_element_by_css_selector("button").click()

    time.sleep(1.5)

    driver.find_element_by_id("q-screening-privacy-statement").click()
    driver.find_element_by_id("q-screening-eligibility-age-range-18 and older").click()
    dropdown = Select(driver.find_element_by_id("q-screening-eligibility-county"))
    dropdown.select_by_visible_text(county)
    driver.find_element_by_id("q-screening-different-county-No").click()
    driver.find_element_by_id("q-screening-18-yr-of-age").click()
    driver.find_element_by_id("q-screening-health-data").click()
    driver.find_element_by_xpath('//button[text()="Continue"]').click()

    time.sleep(1.5)

    location = driver.find_element_by_id("location-search-input")
    location.clear()
    location.send_keys(zip_code)
    driver.find_element_by_xpath('//button[text()="Continue"]').click()

    time.sleep(1.5)

    if (vac_site in driver.page_source):
        break
