# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from configparser import ConfigParser
from config.config import PageElementLocatorPath

class LocatorFile(object):

    def __init__(self):
        self.arg = ConfigParser()
        self.arg.read(PageElementLocatorPath,encoding="utf-8")

    def get_LocatorItems(self, LocatorName):
        locator_obj = dict(self.arg.items(LocatorName))
        return locator_obj

if __name__ == "__main__":
    
    arg = ConfigParser()
    arg.read(PageElementLocatorPath)
    print(dict(arg.items("163mail_login")))