# Spidigo Ahmedabad Login Python Script
The repository for the python script which is used to automate the login

This script is made on top of Python with Selenium. The script just finds the username and password fields on the spidigo.login page and fills it, with the given information.
In order to run this script you need to have Python installed on your PC with Selenium.
To install Python see the link below-

http://www.howtogeek.com/197947/how-to-install-python-on-windows/

To install Selenium see this link-

https://pypi.python.org/pypi/selenium

After successful installation save the script given below with somename.py 
Now go to your terminal, then to your directory where you have saved your file and write: python somename.py
Voila, it works. ENJOY!

THE SCRIPT:-(COPY THE CODE FROM BELOW LINE, change your username and password.)

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://spidigo.login/")    #Spidigo-URL

    def test_Login(self):
        driver          = self.driver
        username        = "abc"                     #Here goes your Spidigo-Username
        password        = "xyz@123"                 #Here goes your Spidigo-Password
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
    
(COPY TILL ABOVE LINE)
