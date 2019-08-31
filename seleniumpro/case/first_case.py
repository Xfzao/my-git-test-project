#coding=utf-8
import sys
sys.path.append("D:\\MyPythonPro\\seleniumpro")


from selenium import webdriver
from business.register_business import RegisterBusiness
import HTMLTestRunner
import os
import time
import unittest


class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.register = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + '/report/' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
        print("后置条件")

    #邮箱错误测试用例
    def test_login_email_error(self):
        email_error = self.register.login_email_error("12436@qq.com", "124356", "67321", "5623")
        self.assertEqual(email_error, "用例执行成功")

    #用户名输入错误测试用例
    def test_login_username_error(self):
        username_error = self.register.login_username_error("12436@qq.com", "12", "67321", "5743")
        self.assertEqual(username_error, "用例执行成功")

    #密码输入错误测试用例
    def test_login_password_error(self):
        password_error = self.register.login_password_error("12436@qq.com", "12457", "673", "5633")
        self.assertEqual(password_error, "用例执行成功")

    #验证码输入错误测试用例
    def test_login_code_error(self):
        code_error = self.register.login_code_error("12436@qq.com", "124356", "67321", "3")
        self.assertEqual(code_error, "用例执行成功")

    #登录成功测试用例
    def test_login_success(self):
        self.register.user_base('87633@163.com', '980763', '77777', '0098')
        succes = self.register.register_succes()
        self.assertEqual(succes, "用例执行成功")
        time.sleep(5)

'''
def main():
    fs = FirstCase()
    fs.test_login_code_error()
    fs.test_login_email_error()
    fs.test_login_password_error()
'''

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report/" + "first_case.html")
    f = open(file_path, 'wb')
    suit = unittest.TestSuite()
    suit.addTest(FirstCase('test_login_email_error'))
    suit.addTest(FirstCase('test_login_username_error'))
    suit.addTest(FirstCase('test_login_password_error'))
    suit.addTest(FirstCase('test_login_code_error'))
    suit.addTest(FirstCase('test_login_success'))
    #unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream = f, title = "first case", description = "第一个测试报告", verbosity = 2)
    runner.run(suit)