from selenium import webdriver
from unittest import TestCase
from xy_case import case
from xy_main import main
from ddt import ddt
from ddt import data

@ddt
class test1(TestCase):

    @data(*case.login_success_data)
    def testcasesuccess(self,testdata):
        username = testdata["username"]
        passwork = testdata["passwork"]
        expect = testdata["expect"]

        driver = webdriver.Chrome()
        loginop = main(driver)
        loginop.login(username,passwork)

        result = loginop.getSuccess_result()
        if result != expect:
            driver.save_screenshot("img/error.png")
        driver.quit()
        self.assertEqual(expect,result)
