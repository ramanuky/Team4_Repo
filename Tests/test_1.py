from Pages.home import Home
from Pages.searchResult import SearchResult
import config
import testdata
import logging
import time


def test(driver):
    h = Home(driver)
    sr = SearchResult(driver)
    h.geturl(config.base_url)
    h.search(testdata.search_text)
    sr.findBrandandClick(testdata.brand_text)
    time.sleep(0.5)
    sr.findPriceandClick(testdata.price_text)
    json = sr.getAndCheckResult()
    

  
