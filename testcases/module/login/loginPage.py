# -- coding: utf-8 --
from testcases.common.commonPage import commonPage

class loginPage(commonPage):

    def login(self,username,password):
        self.login_action(username,password)