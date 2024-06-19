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

    def locelement(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(
            EC.element_to_be_clickable(loc))
        logging.info("Given brand located")
        return elem

    def getElementValue(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc))
        value = elem.get_attribute('value')
        logging.info("Element value get")
        return value

    def findandclick(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(
            EC.element_to_be_clickable(loc))
        elem.click()
        logging.info("Element clicked")

    def find_input_search(self, loc, inputtext, sec=10):
        input_field = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc))
        input_field.clear()
        input_field.send_keys(inputtext)
        input_field.send_keys(Keys.ENTER)
        logging.info("Input field located and text was filled")

    def find_element(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc))
        logging.info("Element located")
        return elem

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

    def currentUrl(self):
        return self.driver.current_url
