# -- coding: utf-8 --
from testcases.common.basePage import basePage
from selenium.webdriver.support.select import By
import logging

class commonPage(basePage):
    username_loc = (By.ID,"username")
    pwd_loc = (By.ID,"pwd")
    loginBtn_loc = (By.CLASS_NAME,"login-button")
    upara = ""

    def login_action(self,username,password):
        self.open(self.upara)
        self.driver.find_element(*self.username_loc).clear()
        self.driver.find_element(*self.username_loc).send_keys(username)
        print(self.driver.find_element(*self.username_loc).is_displayed())
        self.driver.find_element(*self.pwd_loc).send_keys(password)
        self.driver.find_element(*self.loginBtn_loc).click()
        logging.info("已登录")