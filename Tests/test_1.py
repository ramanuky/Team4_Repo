import pytest
import allure
from Pages.home import Home
from Pages.searchResult import SearchResult
import config
import testdata
import time


@allure.feature('Product Search')
@allure.story('Check the Product Search by Brand')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_functionality(driver):
    with allure.step("Open base URL"):
        home_page = Home(driver)
        home_page.geturl(config.base_url)

    with allure.step("Search for product"):
        home_page.search(testdata.search_text)

    with allure.step("Select brand"):
        search_result_page = SearchResult(driver)
        search_result_page.findBrandandClick(testdata.brand_text)
        time.sleep(0.5)

    with allure.step("Select price range"):
        search_result_page.findPriceandClick(testdata.price_text)

    with allure.step("Check search result"):
        json = search_result_page.getAndCheckResult()
        print("json from test_1:", json)

    with allure.step("Verify product details"):
        product = search_result_page.getAndCheckResult()
        assert product is not None, "Product details could not be retrieved"
        assert testdata.brand_text in product['brand_name'], \
            f"Expected '{testdata.brand_text}' to be in '{product['brand_name']}"
        assert product['price'] <= float(testdata.price_text), \
            "Price does not match"
