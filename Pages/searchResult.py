from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging
import time
import requests
from bs4 import BeautifulSoup
import json

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
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # Fetch the webpage content with headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the div with id 'products'
        products_div = soup.find('div', id='products')

        # Check if the div was found and contains the script tag
        if products_div:
            script_tag = products_div.find('script', type='application/ld+json')
            if script_tag:
                # Extract and print the JSON content
                json_content = script_tag.string
                print(type(json_content))
                time.sleep(1)
                data = json.loads(json_content)
                print(type(data))
                product = {}
                product['brand_name'] = data['brand']['name']
                product['price'] = float((data['offers']['price'])[1:])
                print(product)

            else:
                print("Script tag with type 'application/ld+json' not found within the 'products' div.")
        else:
            print("Div with id 'products' not found.")
        
        return product