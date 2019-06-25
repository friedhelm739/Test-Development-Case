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

class WriteLetterPage(object):

    def __init__(self, driver):

        self.driver = driver
        locator = LocatorFile()
        self.locator_dict = locator.get_LocatorItems("163mail_WriteLetterPage")

    
    def SwitchToSelectFrame(self):
        
        try:
            locateType, locateValue = self.locator_dict["WriteLetterPage.frame".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            self.driver.switch_to.frame(element_obj)
        except Exception as error:
            raise error


    def SwitchToDefaultFrame(self):
        
        try:
            self.driver.switch_to.default_content()
        except Exception as error:
            raise error


    def LetterRecipientObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["WriteLetterPage.LetterRecipient".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def LetterTopicObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["WriteLetterPage.LetterTopic".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def LetterContentObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["WriteLetterPage.LetterContent".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def LetterSentObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["WriteLetterPage.LetterSent".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error


    def NoTopicObj(self):
        
        try:
            locateType, locateValue = self.locator_dict["WriteLetterPage.NoTopic".lower()].split(">")
            element_obj = get_element(self.driver, locateType= locateType, locateValue= locateValue)
            return element_obj
        except Exception as error:
            raise error           