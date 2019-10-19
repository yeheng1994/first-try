import ddt
from selenium import webdriver
import time
import unittest
import os  

curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #获取到case的路径

ddt.data(
    {"user":"yeheng","psw":"123456","expect":"ok"},
    {"user":"yeheng","psw":"","expect":"flase"})

if __name__ == "__main__":
  #  filepath = "H:\\Codeall\\WebZd\\Sqldata\\Logindata.xlsx"

    filepath = os.path.jion
    data = ExcelUtil(filepath)
    print(data.dict_data())