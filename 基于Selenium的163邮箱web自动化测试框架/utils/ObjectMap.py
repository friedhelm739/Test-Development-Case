# encoding = utf-8

# import sys
# sys.path.append("../")
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)    # VScode 存在路径bug，通过“../”不能获取相对路径

from config.config import MaxTimeToResponse
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_element(driver, locateType, locateValue):

    try:
        element = WebDriverWait(driver, MaxTimeToResponse).until(lambda _driver: _driver.find_element(by = locateType, value = locateValue))
        return element
    except Exception as error:
        raise error
    driver.find_element

def get_elements(driver, locateType, locateValue):

    try:
        elements = WebDriverWait(driver, MaxTimeToResponse).until(lambda _driver: _driver.find_elements(by = locateType, value = locateValue))
        return elements
    except Exception as error:
        raise error


if __name__ == "__main__":
    
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    time.sleep(3)
    get_element(driver, "id", "kw").send_keys("abcdefg") 
    time.sleep(3)
    driver.close()