# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

import time
import pandas as pd

from PageObject.LoginPage import LoginPage
from config.config import logintest
from TestAction.HomeAction import HomeAction
from PageObject.ContactPage import ContactPage
from TestAction.LoginAction import LoginAction

class ContactAction(object):

    def __init__(self, driver):

        self.driver = driver
        self.CP = ContactPage(self.driver)


    def add_contact(self, contactName, contactEmail, isStar, contactPhone, contactComment):

        try:
            # 单击添加联系人
            
            self.CP.addNewContactObj().click()
            
            if not pd.isnull(contactName):
                self.CP.ContactNewNameObj().send_keys(contactName) 
            # 邮箱为必填
            self.CP.ContactNewEmailObj().send_keys(contactEmail) 

            if not pd.isnull(isStar) and isStar=="是":
                self.CP.ContactNewStarObj().click()

            if not pd.isnull(contactPhone):    
                contactPhone = str(int(contactPhone))
                self.CP.ContactNewPhoneObj().send_keys(contactPhone) 

            if not pd.isnull(contactComment):   
                self.CP.ContactNewCommetObj().send_keys(contactComment) 

            self.CP.ContactToSaveObj().click()      
        except Exception as error:
            raise error


if __name__ == "__main__":
    
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://email.163.com")
    Log = LoginAction(driver)

    time.sleep(1)
    Log.login(Username=logintest["username"], Password=logintest["password"])

    time.sleep(1)
    HP = HomeAction(driver)
    HP.click_Mail_list()
    
    time.sleep(1)
    CA = ContactAction(driver)
    CA.add_contact("xxx", "xxx", True, "xxx", "xxx")

    time.sleep(10)
    driver.close()