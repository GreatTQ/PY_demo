import unittest
from TestDemo.test_case.test01 import Test_log
from HtmlTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_log("test_log"))
runner = HTMLTestRunner()
runner.run(suite)