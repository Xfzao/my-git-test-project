#coding=utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    #获取邮箱输入框元素
    def get_email_element(self):
        return self.fd.get_element("user_email")

    #获取用户名输入框元素
    def get_name_element(self):
        return self.fd.get_element("user_name")

    #获取密码输入框元素
    def get_password_element(self):
        return self.fd.get_element("password")

    #获取验证码输入框元素
    def get_code_element(self):
        return self.fd.get_element("code_text")

    #获取登录按钮元素
    def get_button_element(self):
        return self.fd.get_element("register_button")

    #获取邮箱输入错误提示元素
    def get_email_error(self):
        return self.fd.get_element("email_error")

    #获取用户名输入错误提示元素
    def get_username_error(self):
        return self.fd.get_element("username_error")

    #获取密码输入错误提示元素
    def get_password_error(self):
        return self.fd.get_element("password_error")

    #获取验证码输入错误提示元素
    def get_code_error(self):
        return self.fd.get_element("code_text_error")