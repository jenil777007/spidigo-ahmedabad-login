from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://spidigo.login/")    #Spidigo-URL

    def test_Login(self):
        driver          = self.driver
        username        = "abc"                     #Your Spidigo-Username goes here
        password        = "xyz@123"                 #Your Spidigo-Password goes here
        usernameFieldID = "username"                #Text input id
        passwordFieldID = "password"                #Text input id
        loginid         = "btnLogin"                #Button id

        driver.find_element_by_id(usernameFieldID).clear()
        driver.find_element_by_id(usernameFieldID).send_keys(username)
        driver.find_element_by_id(passwordFieldID).clear()
        driver.find_element_by_id(passwordFieldID).send_keys(password)
        driver.find_element_by_id(loginid).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
