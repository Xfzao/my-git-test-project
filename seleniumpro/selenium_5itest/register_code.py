#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from selenium_5itest.ShowapiRequest import ShowapiRequest


driver = webdriver.Chrome()
#初始化浏览器
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

#获取元素信息
def get_element(id):
    return driver.find_element_by_id(id)

#获取随机数
def get_range_user():
    return ''.join(random.sample('123456789abcdefghijklmn', 8))

#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)

#解析验证码图片
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "100948", "63ad6f9c72d444cd80fe13ec216e3e9a")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", file_name)
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text

#主程序运行
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + "qq.com"
    file_name = r"D:\MyPythonPro\seleniumpro\image\test01.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("123654")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn")
    driver.close()

run_main()