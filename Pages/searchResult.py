from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging
import time
import requests
from bs4 import BeautifulSoup
import json


class SearchResult(Basic_Helper):

    brands_loc = (
        By.XPATH, "//div[@role='group']/ul[@aria-labelledby=\
            'brandNameFacet']/li/a")
    price_loc = (
        By.XPATH, "//div[@role='group']/ul[@aria-labelledby=\
            'priceFacet']/li/a")
    products_loc = (
        By.XPATH, "//div[@id='products']/script[@type=\
            'application/ld+json']")

    def findBrandandClick(self, brand_text):
        brand_names = self.find_elements(self.brands_loc)
        for brand in brand_names:
            if brand_text in brand.text:
                brand.click()
                logging.info(f"Brand '{brand.text}' was found and clicked")
                return
        logging.warning(f"Brand '{brand_text}' not found")

    def findPriceandClick(self, price_text):
        prices = self.find_elements(self.price_loc)
        for price in prices:
            if price_text in price.text:
                price.click()
                logging.info(f"Price '{price.text}' was found and clicked")
                return
        logging.warning(f"Price '{price_text}' not found")

    def getAndCheckResult(self):
        url = self.currentUrl()
        print("URL: ", url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
                    Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        products_div = soup.find('div', id='products')

        if products_div:
            script_tag = products_div.find(
                'script', type='application/ld+json')
            if script_tag:
                json_content = script_tag.string
                time.sleep(1)
                data = json.loads(json_content)
                product = {}
                product['brand_name'] = data['brand']['name']
                product['price'] = float((data['offers']['price'])[1:])
                logging.info(f"Product data extracted: {product}")
                return product
            logging.warning(
                "Script tag with 'application/ld+json' \
                    not found within 'products' div")
        else:
            logging.warning("Div with id 'products' not found")
        return None
