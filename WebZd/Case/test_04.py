#coding:utf-8
from selenium.webdriver.support import  expected_conditions as exC
from selenium import  webdriver

driver =webdriver.Firefox()
driver.get("https://www.baidu.com")

r1 = exC.title_is("百度一下，你就知道")(driver)
print(r1)

r2 = exC.title_contains("小马")(driver)
print(r2)


