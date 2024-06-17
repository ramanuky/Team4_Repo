from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging
import config

class Home(Basic_Helper):
    search_loc = (By.XPATH, "//*[@id='searchAll']")
    
    def search(self, search_text):
        self.findandinput(self.search_loc, search_text)
        current_URL = self.currentURL()
        assert current_URL == config.searched_url, logging.error("Redirected to wrong page")
        logging.info("Successfully redirected to searched text page")
    

    


