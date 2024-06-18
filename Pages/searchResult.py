from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging
import time
import requests
from lxml import html

class SearchResult(Basic_Helper):

    brands_loc = (By.XPATH, "//div[@role='group']/ul[@aria-labelledby='brandNameFacet']/li/a")
    price_loc = (By.XPATH,"//div[@role='group']/ul[@aria-labelledby='priceFacet']/li/a")
    products_loc = (By.XPATH, "//div[@id='products']/script[@type='application/ld+json']")

    def findBrandandClick(self, brand_text):
        brand_names = self.find_elements(self.brands_loc)
        for brand in brand_names:
            if brand_text in brand.text:
                brand.click()
                print(brand.text)
                logging.info("Brand was found")
                break

    def findPriceandClick(self, price_text):
        prices = self.find_elements(self.price_loc)
        for price in prices:
            if price_text in price.text:
                price.click()
                print(price.text)
                logging.info("Price was found")
                break

    def getAndCheckResult(self):
        #products = self.find_elements(self.products_loc)
        # URL of the webpage you want to scrape
        url = self.currentUrl()
        print("url: ", url)
        # Fetch the webpage content
        response = requests.get(url)

        # Parse the HTML content using lxml
        tree = html.fromstring(response.content)

        # Extract the JSON content using XPath

        json_content = tree.xpath(self.products_loc)[0]

        # Print the JSON content
        print("json: ", str(json_content))
