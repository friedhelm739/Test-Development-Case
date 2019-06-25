# encoding = utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

import logging
import datetime
import os
from config.config import logfileBaseDir

logfileBaseDir
class Log(object):

    def __init__(self):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        Logdir = self.getLogdir()
        self.file_handle = logging.FileHandler(Logdir,encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s -----> %(funcName)s: %(levelname)s %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)


    def getLogdir(self):

        log_file_name = datetime.datetime.now().strftime("%Y-%m-%d") +'.log'
        Logdir = os.path.join(logfileBaseDir, log_file_name)
        return Logdir


    def _close_logger(func):
        def wrapper(self, *args, **kwargs):
            print(123)
            func(self, *args, **kwargs)
            self.file_handle.close()
            self.logger.removeHandler(self.file_handle)
            print(123)
        return func


    @_close_logger
    def get_logger_with_close(self):
        return self.logger


    def get_logger(self):
        return self.logger


    def close_logger(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)        


if __name__ == "__main__":
    
    _Log = Log()
    logger = _Log.get_logger_with_close()
    logger.debug("123456")