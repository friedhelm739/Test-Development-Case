# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

import time
import pandas as pd

from PageObject.LoginPage import LoginPage
from config.config import logintest
from PageObject.HomePage import HomePage
from PageObject.ContactPage import ContactPage
from TestAction.LoginAction import LoginAction

class HomeAction(object):


    def __init__(self, driver):

        self.driver = driver
        self.HP = HomePage(self.driver)

    
    def click_Mail_list(self):

        try:
            # 在主页上单击通讯录
            self.HP.ContactModuleObj().click()
        except Exception as error:
            raise error           


    def click_WriteLetter(self):

        try:
            # 在主页上单击写信
            self.HP.WriteLetterObj().click()
        except Exception as error:
            raise error   

if __name__ == "__main__":
    
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://email.163.com")
    Log = LoginAction(driver)

    time.sleep(1)
    Log.login(Username=logintest["username"], Password=logintest["password"])

    HA = HomeAction(driver)
    HA.click_Mail_list()

    time.sleep(10)
    driver.close()