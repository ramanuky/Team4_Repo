from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging
import config


class Home(Basic_Helper):
    search_loc = (By.XPATH, "//*[@id='searchAll']")

    def search(self, search_text):
        self.find_input_search(self.search_loc, search_text)
        logging.info("Search text entered.")

        current_url = self.driver.current_url

        if config.searched_url == current_url:
            logging.info(
                f"Successfully redirected to search results page. \
                    Current URL: {current_url}")
        else:
            logging.warning(
                f"Redirection to search results page failed. \
                    Current URL: {current_url}")
