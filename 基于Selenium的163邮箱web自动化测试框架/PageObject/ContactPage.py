# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from utils.ObjectMap import *
from utils.DealconfigFile import LocatorFile
import time
from config.config import logintest


class ContactPage(object):

    def __init__(self, driver):

        self.driver = driver
        locator = LocatorFile()
        self.locator_dict = locator.get_LocatorItems("163mail_addContactsPage")


    def addNewContactObj(self):

        try:
            locateType, locateValue = self.locator_dict["ContactsPage.addNewContact".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def ContactNewNameObj(self):

        try:
            locateType, locateValue = self.locator_dict["ContactsPage.ContactNewName".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error

 
    def ContactNewEmailObj(self):

        try:
            locateType, locateValue = self.locator_dict["ContactsPage.ContactNewEmail".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def ContactNewStarObj(self):

        try:
            locateType, locateValue = self.locator_dict["ContactsPage.ContactNewStar".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def ContactNewPhoneObj(self):

        try:
            locateType, locateValue = self.locator_dict["ContactsPage.ContactNewPhone".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def ContactNewCommetObj(self):

        try:
            locateType, locateValue = self.locator_dict["ContactsPage.ContactNewCommet".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def ContactToSaveObj(self):

        try:
            locateType, locateValue = self.locator_dict["ContactsPage.ContactToSave".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


if __name__ == "__main__":
    
    from selenium import webdriver
    from TestAction.LoginAction import LoginAction
    from HomePage import HomePage
    driver = webdriver.Chrome()
    driver.get("https://email.163.com")
    Log = LoginAction()

    time.sleep(1)
    Log.login(driver, Username=logintest["username"], Password=logintest["password"])

    time.sleep(5)
    HP = HomePage(driver)
    HP.ContactModuleObj().click()

    time.sleep(1)
    CP = ContactPage(driver)

    CP.addNewContactObj().click()
    CP.ContactNewNameObj().send_keys("姚文轩") 
    CP.ContactNewEmailObj().send_keys("2622872048@qq.com") 
    CP.ContactNewStarObj().click()
    CP.ContactNewPhoneObj().send_keys("1556622817") 
    CP.ContactNewCommetObj().send_keys("这是一次测试") 
    CP.ContactToSaveObj().click()

    time.sleep(10)
    driver.close()
