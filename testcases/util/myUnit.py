# -- coding: utf-8 --
import unittest
from selenium import webdriver

class driverUnit(unittest.TestCase):
    fp = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(firefox_profile=fp)

    @classmethod
    def setUpClass(cls):
        print("start...")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        print("end...")

