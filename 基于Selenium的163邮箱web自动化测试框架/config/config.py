# encoding = utf-8

import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
PageElementLocatorPath = os.path.join(BASE_DIR,"config/PageElementLocator.ini")

MaxTimeToResponse = 30

# Login Test
logintest = {"username":"friedhelm739", "password":"ywx_xsqq39"}

# Log File
logfileBaseDir = os.path.join(BASE_DIR,"Data")

LoginExcelDir = r"E:\缓存文件\VScode\163test\Data\163账号.xlsx"
ContactExcelDir = r"E:\缓存文件\VScode\163test\Data\联系人.xlsx"

LoginTestExcelDir = r'E:\缓存文件\VScode\163test\Data\LoginTest.xls'
WriteLetterTestExcelDir = r'E:\缓存文件\VScode\163test\Data\WriteLetterTest.xls'

HTMLlogDir = r'E:\缓存文件\VScode\163test\Data\report.html'

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