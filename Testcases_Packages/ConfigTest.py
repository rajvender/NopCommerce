from  selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome("H:\Drivers\chromedriver.exe")
    return driver