#coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mail.163.com")

driver.find_element_by_id("switchAccountLogin").click()

driver.switch_to.frame(driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]'))
driver.find_element_by_name("email").send_keys("181859662053")
driver.find_element_by_name("password").send_keys("xfz513798426")
driver.find_element_by_id("dologin").click()

#driver.quit()