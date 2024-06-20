import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException


class Basic_Helper:
    def __init__(self, driver):
        self.driver = driver

    def geturl(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info(f"Open url {url}")

    def currentUrl(self):
        return self.driver.current_url
    
    def find_input_search(self, loc, inputtext, sec=10):
        input_field = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc))
        input_field.clear()
        input_field.send_keys(inputtext)
        input_field.send_keys(Keys.ENTER)
        logging.info("Input field located and text was filled")

    def find_elements(self, loc, sec=10):
        try:
            elements = WebDriverWait(self.driver, sec).until(
                EC.presence_of_all_elements_located(loc))
            logging.info("Elements located")
            return elements
        except StaleElementReferenceException:
            elements = WebDriverWait(self.driver, sec).until(
                EC.presence_of_all_elements_located(loc))
            logging.info("Elements located after retry")
            return elements

