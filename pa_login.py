from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

import os


def login(user, password):

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("https://private.best.eu.org/welcome.jsp")

    assert "BEST Private Area" in driver.title, "This should lead to the BEST Private Area!"

    driver.find_element_by_id("loginFormName").send_keys(user)
    driver.find_element_by_id("loginFormPass").send_keys(password)
    driver.find_element_by_xpath('//button[text()="Login"]').click()

    return driver


if __name__ == "__main__":
    PA_USER = os.environ.get("PA_USER")
    PA_PASSWORD = os.environ.get("PA_PASS")

    browser = login(PA_USER, PA_PASSWORD)
