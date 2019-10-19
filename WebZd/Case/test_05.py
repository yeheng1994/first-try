#coding:utf-8
from selenium import webdriver
import time

url = "https://cd.meituan.com/"
driver = webdriver.Firefox()
driver.get(url)

time.sleep(1)
driver.find_element_by_xpath("//*[text()='酒店'and@class='link nav-text']").click()
time.sleep(1)

tle = driver.title  #获取当前窗口
print(tle)
#获取，切换新窗口
h1 = driver.current_window_handle
print(h1)
'''new_handle = all[-1]
driver.switch_to.window(new_handle)
t2 = driver.title
print(t2)'''


driver.switch_to.window(driver.window_handles[-1])
t2 = driver.title
print(t2)

driver.find_element_by_xpath("//*[@placeholder='(关键词选填) 酒店名/位置/品牌']").send_keys("春熙路")
time.sleep(1)
driver.find_element_by_class_name("search-btn").click()
#driver.find_element_by_xpath("html/body/mieta/main/section/section/div[1]/div/div/input").click()
#获取所有窗口
#all = driver.window_handles
#print(all)


#driver.close()

#当有iframe上操作元素需要进行切换和切回
'''
driver.switch_to.frame("id")
driver.find_element_by_css_selector("")
driver.switch_to.default_content()
'''