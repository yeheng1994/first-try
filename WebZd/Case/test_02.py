import unittest
from selenium import webdriver
from Case.test_login import login
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_login_1(self):
        login(self.driver)  #登录功能
