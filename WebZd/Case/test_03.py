# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(20)
# 鼠标移动到“设置”按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()

time.sleep(1)
# 判断搜索设置的属性
s = driver.find_element_by_link_text("搜索设置")
print(s.is_displayed())  # 判断元素显示出来了
