#coding=utf-8

from selenium import webdriver
import time
from PIL import Image
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_5itest.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))

#获取验证码
driver.save_screenshot("D:/MyPythonPro/seleniumpro/image/5itest2.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open("D:/MyPythonPro/seleniumpro/image/5itest2.png")
img = im.crop((left, top, right, height))
img.save("D:/MyPythonPro/seleniumpro/image/5itest3.png")

#解析验证码
r = ShowapiRequest("http://route.showapi.com/184-4", "100948", "63ad6f9c72d444cd80fe13ec216e3e9a")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"D:/MyPythonPro/seleniumpro/image/5itest3.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text)


#随机数生成用户名
user_email = ''.join(random.sample("0123456789", 8)) + "@163.com"

#判断元素是否可见
locator = (By.CLASS_NAME, "controls")
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
email_element = driver.find_element_by_id("register_email")

#输入用户名和获取元素中的信息
print(email_element.get_attribute("placeholder"))
email_element.send_keys(user_email)
print(email_element.get_attribute("value"))


#driver.find_element_by_name("email").send_keys(user_email)
user_name_element_code = driver.find_elements_by_class_name("controls")[1]
user_element = user_name_element_code.find_element_by_class_name("form-control")
user_element.send_keys("Xiao")
driver.find_element_by_xpath("//*[@id='register_password']").send_keys("x123654")
driver.find_element_by_id("captcha_code").send_keys(text)
driver.close()