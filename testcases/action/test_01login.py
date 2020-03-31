# -- coding: utf-8 --
from testcases.common.commonPage import commonPage
from testcases.util.myUnit import driverUnit
from testcases.module.login.loginPage import loginPage
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import By
from time import sleep
import re
import requests
from ruamel import yaml


class test_login(driverUnit):
    po = loginPage(driverUnit.driver)
    username_loc = (By.ID,"username")


    def test_00login(self):
        self.po.login("admin","123456")

if __name__ == '__main__':
    unittest.main()
