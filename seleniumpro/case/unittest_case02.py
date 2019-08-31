# -*-coding:utf-8 -*-
import unittest
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


class FirstCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有case执行前的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行后的后置")

    def setUp(self):
        print("这是前置条件")

    def tearDown(self):
        print("这是后置条件")

    def test_first001(self):
        print("第一条测试用例")

    @unittest.skip("不执行")
    def test_first002(self):
        print("第二条测试用例")

    def test_first003(self):
        print("第三条测试用例")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('test_first002'))
    suite.addTest(FirstCase02('test_first001'))
    suite.addTest(FirstCase02('test_first003'))
    unittest.TextTestRunner().run(suite)
