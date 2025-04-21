import logging
from selenium import webdriver
import pytest


@pytest.fixture()
def selenium(pytestconfig):
    options = webdriver.ChromeOptions()
    logging.info("Prepare browser")
    driver = webdriver.Chrome(options=options)
    # if pytestconfig.getini("headless") == "True":
    #     options.add_argument("--headless=new")
    # options.browser_version = pytestconfig.getini("browser_version")
    # driver = webdriver.Remote(
    #     command_executor=pytestconfig.getini("selenium_url"),
    #     options=options,

    # )
    driver.set_window_size(1400, 770)
    logging.info("Browser has been started")
    yield driver
    driver.quit()
