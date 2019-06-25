# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from configparser import ConfigParser
from config.config import ContactSheetFormat
import pandas as pd

class DealExcelFile(object):

    def __init__(self):
        self.header = True

    def load(self, path):

        try:
            self.xls = pd.read_excel(path)
            self.save_path = path
            return self.xls.copy()
        except Exception as error:
            raise error


    def getLenth(self):

        return len(self.xls)


    def getSheet(self, index):

        try:
            return self.xls.iloc[index,:].copy()
        except Exception as error:
            raise error


    def getListSheet(self):

        result = []
        for index in range(self.getLenth()):
            result.append(self.xls.iloc[index,:].copy())
        return result

    def saveSheet(self, sheet, path = None):    

        if path is None:
            path = self.save_path.split(".")[0] + '.csv'
        try:
            sheetToSave = pd.DataFrame(sheet).T   
            sheetToSave.to_csv(path, mode="a", header=self.header, index=False) 
            self.header = False
        except Exception as error:
            raise error


if __name__ == "__main__":

    deal = DealExcelFile()
    _ = deal.load(r'E:\缓存文件\VScode\163test\Data\联系人.xlsx')
    for i in range(5):

        print(deal.getSheet(i))
        sheet = deal.getSheet(i)
        sheet[0] = 100 + i
        deal.saveSheet(sheet)