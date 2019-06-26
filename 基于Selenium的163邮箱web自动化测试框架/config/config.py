# encoding = utf-8

import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
PageElementLocatorPath = os.path.join(BASE_DIR,"config/PageElementLocator.ini")

MaxTimeToResponse = 30

# Login Test
logintest = {"username":"XXX", "password":"XXX"}

# Log File
logfileBaseDir = os.path.join(BASE_DIR,"Data")

LoginExcelDir = r"E:\缓存文件\VScode\基于Selenium的163邮箱web自动化测试框架\Data\163账号.xlsx"
ContactExcelDir = r"E:\缓存文件\VScode\基于Selenium的163邮箱web自动化测试框架\Data\联系人.xlsx"

LoginTestExcelDir = r'E:\缓存文件\VScode\基于Selenium的163邮箱web自动化测试框架\Data\LoginTest.xls'
WriteLetterTestExcelDir = r'E:\缓存文件\VScode\基于Selenium的163邮箱web自动化测试框架\Data\WriteLetterTest.xls'

HTMLlogDir = r'E:\缓存文件\VScode\基于Selenium的163邮箱web自动化测试框架\Data\report.html'

# 为方便扩展可将header名改为别名
ContactSheetFormat = {  "ContactName":1, 
                        "ContactEmail":2, 
                        "ContactStar":3, 
                        "ContactPhone":4, 
                        "ContactComment":5,
                        "KeyWord":6,
                        "IsDeal":7,
                        "DealingTime":8,
                        "TestResult":9 }
