from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://spidigo.login/")

    def test_Login(self):
        driver = self.driver
        fbusername = "karanmodi"
        fbpassword = "86610"
        emailFieldID = "username"
        passFieldID = "password"
       # loginButtonXPath = "//input[@value='Log In']"
        loginid = "btnLogin"
      #  facebookLogoXPath =

      #  efe = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(efe))
       # pfe = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(pfe))
        #loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))

        driver.find_element_by_id(emailFieldID).clear()
        driver.find_element_by_id(emailFieldID).send_keys(fbusername)
        driver.find_element_by_id(passFieldID).clear()
        driver.find_element_by_id(passFieldID).send_keys(fbpassword)
        driver.find_element_by_id(loginid).click()

       # efe.clear()
       # efe.send_keys(fbusername)
       # pfe.clear()
       # pfe.send_keys(fbpassword)
       # loginButtonElement.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()