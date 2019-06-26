# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from utils.ObjectMap import *
from utils.DealconfigFile import LocatorFile
import time
from config.config import logintest


class HomePage(object):

    def __init__(self, driver):

        self.driver = driver
        locator = LocatorFile()
        self.locator_dict = locator.get_LocatorItems("163mail_homePage")


    def ContactModuleObj(self):

        try:
            locateType, locateValue = self.locator_dict["homePage.ContactModule".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error

        
    def WriteLetterObj(self):

        try:
            locateType, locateValue = self.locator_dict["homePage.WriteLetter".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


if __name__ == "__main__":
    
    from selenium import webdriver
    from TestAction.LoginAction import LoginAction
    driver = webdriver.Chrome()
    driver.get("https://email.163.com")
    Log = LoginAction(driver)

    time.sleep(3)
    Log.login(Username=logintest["username"], Password=logintest["password"])

    time.sleep(5)
    HP = HomePage(driver)
    HP.ContactModuleObj().click()
    
    time.sleep(5)
    driver.close()