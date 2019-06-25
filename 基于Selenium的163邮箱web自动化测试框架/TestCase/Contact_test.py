# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

import unittest
from selenium import webdriver
import time

from TestAction.LoginAction import LoginAction
from TestAction.HomeAction import HomeAction
from TestAction.ContactAction import ContactAction
from utils.DealExcelFile import DealExcelFile
from utils.Log import Log
from utils.ObjectMap import get_element
from config.config import LoginExcelDir, ContactExcelDir
import datetime


class Contact_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Log = Log()
        cls.logger = cls.Log.get_logger()
        cls.LoginExcel = DealExcelFile()
        _ = cls.LoginExcel.load(LoginExcelDir)

        cls.ContactExcel = DealExcelFile()
        _ = cls.ContactExcel.load(ContactExcelDir)

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

    def test_163_AddContact(self):

        for Account_num in range(self.LoginExcel.getLenth()):

            Account = self.LoginExcel.getSheet(Account_num)
            self.logger.info("使用%s账号"%(Account["账号"])) 

            LA = LoginAction(self.driver)
            LA.login(Username=Account["账号"], Password=Account["密码"])
            time.sleep(1)

            if("操作超时，请刷新页面重试" in self.driver.page_source):

                self.logger.info("添加联系人：%s失败，原因：操作超时，请刷新页面重试"%(Contact["联系人姓名"]))
                continue

            HP = HomeAction(self.driver)
            HP.click_Mail_list()
            time.sleep(1)
            CA = ContactAction(self.driver)

            for Contact_num in range(self.ContactExcel.getLenth()):

                Contact = self.ContactExcel.getSheet(Contact_num)

                if(Contact['是否执行'] == "n"):
                    self.logger.info("未添加联系人： %s"%(Contact["联系人姓名"]))  
                    Contact['测试结果'] = None 

                else:
                    CA.add_contact(Contact['联系人姓名'], Contact['联系人邮箱'], Contact['是否星标'], Contact['联系人手机号'], Contact['联系人备注'])
                    time.sleep(1)             
                    try:
                        assert Contact['验证界面包含的关键字'] in self.driver.page_source
                    except: 
                        Contact['测试结果'] = False
                    else:
                        Contact['测试结果'] = True

                    Contact['执行时间'] = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
                    self.logger.info("成功添加联系人： %s"%(Contact["联系人姓名"]))     

                self.ContactExcel.saveSheet(Contact)
                time.sleep(1)

if __name__ == "__main__":
    unittest.main()
        