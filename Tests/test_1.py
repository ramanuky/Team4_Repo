from Pages.home import Home
from Pages.searchResult import SearchResult
import config
import testdata
import time


def test_search_functionality(driver):
    home_page = Home(driver)
    search_result_page = SearchResult(driver)

    home_page.geturl(config.base_url)
    home_page.search(testdata.search_text)
    search_result_page.findBrandandClick(testdata.brand_text)
    time.sleep(0.5)
    search_result_page.findPriceandClick(testdata.price_text)
    json = search_result_page.getAndCheckResult()
    print("json from test_1:", json)

    product = search_result_page.getAndCheckResult()
    assert product is not None, "Product details could not be retrieved"
    assert testdata.brand_text in product['brand_name'], \
        f"Expected '{testdata.brand_text}' to be in '{product['brand_name']}"
    assert product['price'] <= float(testdata.price_text), \
        "Price does not match"
