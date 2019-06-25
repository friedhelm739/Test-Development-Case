# encoding = utf-8

# import sys,os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
# sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

import unittest
import HTMLTestRunner

from TestCase.Contact_test import Contact_test
from TestCase.WriteLetter_test import WriteLetter_test
from TestCase.Login_test import Login_test
from config.config import HTMLlogDir



if __name__ == "__main__":
    
    suite_Contact_test = unittest.TestLoader().loadTestsFromTestCase(Contact_test)
    suite_Login_test = unittest.TestLoader().loadTestsFromTestCase(Login_test)   
    suite_WriteLetter_test = unittest.TestLoader().loadTestsFromTestCase(WriteLetter_test)   

    suite = unittest.TestSuite([suite_WriteLetter_test, suite_Contact_test])
    
    _file = open(HTMLlogDir, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=_file)
    runner.run(suite)
    _file.close()