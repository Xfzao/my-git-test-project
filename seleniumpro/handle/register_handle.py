#coding=utf-8
from page.register_page import RegisterPage
class RegisterHandle(object):
    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    #输入邮箱
    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self, name):
        self.register_p.get_name_element().send_keys(name)

    #输入密码
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    #输入验证码
    def send_user_code(self, code):
        self.register_p.get_code_element().send_keys(code)

    #点击登录
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #获取错误信息
    def get_user_text(self, info):
        try:
            if info == 'user_error':
                text = self.register_p.get_email_error().text
            elif info == 'user_name_error':
                text = self.register_p.get_username_error().text
            elif info == 'password_error':
                text = self.register_p.get_password_error().text
            elif info == 'code_text_error':
                text = self.register_p.get_code_error().text
        except:
            text = None
        return text
    #注册失败错误信息
    def get_register_text(self):
        return self.register_p.get_button_element().text