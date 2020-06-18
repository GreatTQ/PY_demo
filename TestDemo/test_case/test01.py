import unittest
import requests
import json
from TestDemo.tool.fileRead import ReadYaml
from TestDemo.config.config import CONFIG_FILE,REPORT_PATH,DATA_FILE
from TestDemo.tool.log import logger,myLog
from HtmlTestRunner import HTMLTestRunner
from TestDemo.tool.run_method import RunMain

class Test_log(unittest.TestCase):

    @myLog
    def test_log(self):
        url = ReadYaml(CONFIG_FILE).getDatas('URL')
        params = ReadYaml(DATA_FILE).getDatas('qiantao')
        re = RunMain().run_main('GET',url, params)

        self.assertEqual("200", json.loads(re.text).get("resultcode"))
        

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_log("test_log"))
    runner = HTMLTestRunner()
    runner.run(suite)