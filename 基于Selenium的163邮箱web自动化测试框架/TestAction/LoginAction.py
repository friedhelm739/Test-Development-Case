# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from PageObject.LoginPage import LoginPage
from config.config import logintest
import time
import pandas as pd

class LoginAction(object):

    def __init__(self, driver):

        self.driver = driver
        self.Login = LoginPage(self.driver)

    def login(self, Username, Password):

        try:
            self.Login.SwitchToSelectFrame()
            # 输入用户名、密码、点击确定
            if not pd.isnull(Username):
                self.Login.UserNameObj().send_keys(Username) 

            if not pd.isnull(Password):    
                self.Login.PasswordObj().send_keys(Password) 

            self.Login.LoginButtonObj().click()

            self.Login.SwitchToDefaultFrame()            
        except Exception as error:
            raise error


if __name__ == "__main__":
    
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://email.163.com")
    Log = LoginAction(driver)
    time.sleep(1)
    Log.login(Username=logintest["username"], Password=logintest["password"])
    time.sleep(10)
    driver.close()