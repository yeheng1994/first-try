# coding=utf-8
from selenium import webdriver
import unittest
import time

def login(driver):
    driver.get("http://baidu.com")
    driver.find_element_by_id("account").send_keys("yeheng")
    driver.find_element_by_name("password").send_keys("123456")
    driver.find_element_by_id("submit").clink()
if __name__ == "__maim__":
    '''print(dir(__builtins__)) '''
    driver = webdriver.Firefox()
    login(driver)

