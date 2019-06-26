# encoding = utf-8

# import sys
# sys.path.append("../")
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from utils.ObjectMap import *
from utils.DealconfigFile import LocatorFile
import time
from config.config import logintest

class LoginPage(object):

    def __init__(self, driver):

        self.driver = driver
        locator = LocatorFile()
        self.locator_dict = locator.get_LocatorItems("163mail_loginPage")


    def SwitchToSelectFrame(self):
        
        try:
            locateType, locateValue = self.locator_dict["loginPage.frame".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            self.driver.switch_to.frame(element_obj)
        except Exception as error:
            raise error


    def SwitchToDefaultFrame(self):
        
        try:
            self.driver.switch_to.default_content()
        except Exception as error:
            raise error


    def UserNameObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["loginPage.username".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def PasswordObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["loginPage.password".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def LoginButtonObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["loginPage.loginbutton".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


if __name__ == "__main__":
    
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://email.163.com")
    Log = LoginPage(driver)
    time.sleep(1)
    Log.SwitchToSelectFrame()
    Log.UserNameObj().send_keys(logintest["username"]) 
    Log.PasswordObj().send_keys(logintest["password"]) 
    Log.LoginButtonObj().click()
    Log.SwitchToDefaultFrame()
    time.sleep(3)
    driver.close()