# coding=utf-8
from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, name, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()

    #登录成功
    def register_succes(self):
        if self.register_h.get_register_text() == None:
            return "用例执行成功"
        else:
            return "用例执行成功"

    # 邮箱错误
    def login_email_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('email_error') == "请输入有效的电子邮件地址":
            return "用例执行成功"
        else:
            return "用例执行失败"

    # 用户名错误
    def login_username_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('user_name_error') == "字符长度必须大于等于4，一个中文字算2个字符":
            return "用例执行成功"
        else:
            return "用例执行失败"

    # 密码错误
    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('password_error') == "最少需要输入 5 个字符":
            return "用例执行成功"
        else:
            return "用例执行失败"

    # 验证码错误
    def login_code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('code_text_error') == "验证码错误":
            return "用例执行成功"
        else:
            return "用例执行失败"
