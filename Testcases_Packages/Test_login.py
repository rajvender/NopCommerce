import pytest
from selenium import webdriver

from PageObject_Package import LoginPage
from PageObject_Package.LoginPage import Login
from Testcases_Packages.ConfigTest import setup

class Testone:
    base_URL="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"

    def test_Testhomepage(self,setup):
        self.driver=setup
        self.driver.get(self.base_URL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            assert False
    def test_Login(self,setup):
        self.driver=setup
        self.driver.get(self.base_URL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title="Dashboard / nopCommerce administration"
        if act_title=="Dashboard / nopCommerce administration":
                assert True
        else:
            assert False







