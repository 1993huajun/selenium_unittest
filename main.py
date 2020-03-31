# -- coding: utf-8 --
import unittest
from BSTestRunner import BSTestRunner
import time

if __name__ == '__main__':

    testDir = "./testcases/action/"
    discover = unittest.defaultTestLoader.discover(testDir,pattern="test*.py")

    now = time.strftime("%y-%m-%d %H_%M_%S")
    report_dir = "./reports/"
    report_name = report_dir + now + "_result.html"
    with open(report_name,"wb") as file:
        runner = BSTestRunner(stream=file,title="module",description="test report")

        runner.run(discover)
    file.close()

