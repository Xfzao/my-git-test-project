#coding=utf-8
import unittest


class FirstCase01(unittest.TestCase):

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

    def test_first01(self):
        print("第一条测试用例")

    @unittest.skip("不执行")
    def test_first02(self):
        print("第二条测试用例")

    def test_first03(self):
        print("第三条测试用例")

'''
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('test_first02'))
    suite.addTest(FirstCase01('test_first01'))
    suite.addTest(FirstCase01('test_first03'))
    unittest.TextTestRunner().run(suite)
'''