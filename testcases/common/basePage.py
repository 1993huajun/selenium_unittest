# -- coding: utf-8 --

class basePage():
    def __init__(self,driver):
        self.base_url = "url"
        self.driver = driver

    def _open(self,upara):
        self.driver.get(self.base_url+upara)

    def open(self,upara):
        self._open(upara)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
