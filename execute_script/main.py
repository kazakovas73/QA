from selenium import webdriver
import time
import os
from math import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_tag_name("button").click()

    x = int(browser.find_element_by_id("input_value").text)
    y = str(log(abs(12 * sin(x)), e))

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("solve").click()

finally:
    time.sleep(6)
    browser.quit()