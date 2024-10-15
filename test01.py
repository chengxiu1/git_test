import unittest
from time import sleep

from csvv import *
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By

@ddt.ddt
class Denlu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.quit()
    @ddt.data(*read())
    def test_denglu01(self,list):
        self.driver.get('http://192.168.46.5:13077/login')
        self.driver.find_element(By.CLASS_NAME, 'username').send_keys('XTGLY')
        self.driver.find_element(By.ID, 'password').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '商品品牌').click()
        self.driver.find_elements(By.TAG_NAME, 'button')[3].click()
        self.driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys(list[0])
        # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/button[1]').click()
        sleep(2)
        try:
            self.driver.find_element(By.CLASS_NAME, 'el-form-item__error').text
        except:
            self.driver.get_screenshot_as_file("test01.png")
if __name__ == '__main__':
    unittest.main()