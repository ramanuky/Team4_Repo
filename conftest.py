import pytest
from selenium import webdriver
import logging
import allure


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(filename)s:'
               '%(lineno)d - %(funcName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='mylog.log',
        filemode='w+',
        encoding='utf-8'
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        # Attach a screenshot to the Allure report on test failure
        driver = item.funcargs['driver']
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG)
        # Attach the page source to the Allure report on test failure
        allure.attach(
            driver.page_source,
            name="page_source",
            attachment_type=allure.attachment_type.HTML)
