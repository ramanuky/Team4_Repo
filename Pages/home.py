from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging
import config

class Home(Basic_Helper):
    search_loc = (By.XPATH, "//*[@id='searchAll']")
    
    def search(self, search_text):
        self.find_input_search(self.search_loc, search_text)
        # add checking for current url
        logging.info("Successfully redirected to searched text page")
    

    


