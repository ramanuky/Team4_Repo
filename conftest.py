import pytest
from selenium import webdriver
import logging


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
