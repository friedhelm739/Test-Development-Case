# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from PageObject.WriteLetterPage import WriteLetterPage
from TestAction.HomeAction import HomeAction
from TestAction.LoginAction import LoginAction
from config.config import logintest
import time
import pandas as pd

class WriteLetterAction(object):

    def __init__(self, driver):

        self.driver = driver
        self.Letter = WriteLetterPage(self.driver)

    def WriteLetter(self, Recipient, Topic, Content):

        try:
            if not pd.isnull(Recipient):
                self.Letter.LetterRecipientObj().send_keys(Recipient) 

            if not pd.isnull(Topic):    
                self.Letter.LetterTopicObj().send_keys(Topic) 

            self.Letter.SwitchToSelectFrame()
            if not pd.isnull(Content):    
                self.Letter.LetterContentObj().send_keys(Content) 
            self.Letter.SwitchToDefaultFrame()

            self.Letter.LetterSentObj().click()

            if(pd.isnull(Topic)):
                time.sleep(1)
                self.Letter.NoTopicObj().click()
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
    HP.click_WriteLetter()
    
    time.sleep(1)
    WLA = WriteLetterAction(driver)
    WLA.WriteLetter('XXX', '测试', '这是一个测试')

    time.sleep(10)
    driver.close()    


