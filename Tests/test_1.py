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
    assert sr.currentURL()==config.searched_url, logging.error("Invalid url")
    sr.findBrand(testdata.brand_text)
  
