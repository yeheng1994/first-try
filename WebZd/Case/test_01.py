# coding=utf-8
from selenium import webdriver
import unittest
import time

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")

    def test_001(self):
        '''搜索：selenium'''
        self.driver .xxx

    def test_002(self):
        ''' 搜索：python'''
        self.driver.xxx

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()