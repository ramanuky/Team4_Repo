from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging


class SearchResult(Basic_Helper):
   
    brand_loc = (By.XPATH, "//*[@id='searchFilters']/div[1]/div[2]/section[3]/div[2]/ul/li[3]/a/span[1]")
    search_brand_loc = (By.ID, "Brand")
    search_brands_elem_loc = (By.XPATH, "//div[@role='group']/ul[@aria-labelledby='brandNameFacet']/li/a")
    price_loc = (By.XPATH,"//*[@id='searchFilters']/div[1]/div[2]/section[4]/div/ul/li/a/span[1]")

    def findBrand(self, brand_text):
        self.findandinput(self.search_brand_loc, brand_text)
        self.findandclick(self.search_brands_elem_loc)
        logging.info("Successfully found the brand from testdata")
    

    


