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


    with allure.step("Verify product details"):
        product = search_result_page.getAndCheckResult()
        assert product is not None, "Product details could not be retrieved"
        assert testdata.brand_text in product['brand_name'], \
            f"Expected '{testdata.brand_text}' to be in '{product['brand_name']}"
        assert product['price'] <= float(testdata.price_text), \
            "Price does not match"

# Notes - Very interesting approache , I especially like the allure reporting features
# One note according to use beutiful soup and requests library in the test is not a good practice
# because you don't interact with the browser and you don't test the UI, you test the data that is returned from the server
# But it could be good practise if you need to parse the data from the server and do some data manipulation
# Other parts of the test are well written and easy to understand - Good Job  :)