import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), "logging.ini")
logging.config.fileConfig(log_file_path)

pytest_plugins = ["src"]


def pytest_addoption(parser):
    parser.addini("selenium_url", "Selenium Hub url")
    parser.addini("browser_version", "Browser version for tests")
    parser.addini("headless", "Run browser in headless mode")
