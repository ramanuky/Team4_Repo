from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging


class SearchResult(Basic_Helper):
   
    brand_loc = (By.XPATH, "//*[@id='searchFilters']/div[1]/div[2]/section[3]/div[2]/ul/li[3]/a/span[1]")
    price_loc = (By.XPATH,"//*[@id='searchFilters']/div[1]/div[2]/section[4]/div/ul/li/a/span[1]")

    def find(self, email_data, code_data):
        self.findandinput(self.email_loc, email_data)
        self.findandinput(self.code_loc, code_data)
        self.findandclick(self.send_loc)
        logging.info("Successfully passed first login")
    

    


