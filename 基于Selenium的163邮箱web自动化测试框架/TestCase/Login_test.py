# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

import unittest
from selenium import webdriver
import time
import ddt
import datetime

from TestAction.LoginAction import LoginAction
from PageObject.LoginPage import LoginPage
from utils.DealExcelFile import DealExcelFile
from utils.Log import Log
from utils.ObjectMap import get_element
from config.config import LoginTestExcelDir

LoginExcel = DealExcelFile()
_ = LoginExcel.load(LoginTestExcelDir)
data = LoginExcel.getListSheet()

@ddt.ddt
class Login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Log = Log()
        cls.logger = cls.Log.get_logger()


    @classmethod
    def tearDownClass(cls):
        cls.Log.close_logger()


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://email.163.com")
        self.logger.info("打开Chrome浏览器")        


    def tearDown(self):

        self.driver.close()
        self.logger.info("关闭Chrome浏览器")


    @ddt.data(*data)
    def test_163_Login(self, Account):

        if(Account['是否执行'] == 'n'):

            self.logger.info("跳过执行%s账号"%(Account["账号"])) 
            return 
        
        self.logger.info("使用%s账号"%(Account["账号"])) 

        LA = LoginAction(self.driver)
        LG = LoginPage(self.driver)
        LA.login(Username=Account["账号"], Password=Account["密码"])
        time.sleep(1)

        if("操作超时，请刷新页面重试" in self.driver.page_source):
            self.logger.info("添加联系人：%s失败，原因：操作超时，请刷新页面重试"%(Account["账号"]))
            return 
            
        time.sleep(1)
        if("请先进行验证" in self.driver.page_source):
            self.logger.info("添加联系人：%s失败，原因：请先进行验证"%(Account["账号"]))
            return            

        Account['执行时间'] = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        try:
            if(Account['验证界面包含的关键字']!='收件箱'):
                LG.SwitchToSelectFrame()
                time.sleep(2)
            assert Account['验证界面包含的关键字'] in self.driver.page_source
            if(Account['验证界面包含的关键字']!='收件箱'):
                LG.SwitchToDefaultFrame()
        except Exception as error: 
            Account['测试结果'] = False
            LoginExcel.saveSheet(Account)
            self.logger.info("测试失败： %s"%(Account["账号"])) 
            raise error
        else:
            Account['测试结果'] = True

        self.logger.info("成功添加联系人： %s"%(Account["账号"]))     
        LoginExcel.saveSheet(Account)
        time.sleep(5)            


if __name__ == "__main__":
    unittest.main()
        