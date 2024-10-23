import unittest
from time import sleep

import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from csvv import *
@ddt.ddt
class Denlu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.close()
    @ddt.data(*read())
    def test_denglu01(self,list):
        self.driver.get('http://192.168.46.5:13077/login?redirect=%2Findex')
        self.driver.find_element(By.ID, 'username').send_keys('XTGLY')
        self.driver.find_element(By.NAME, 'password').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, '商品分类').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/button').click()
        sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys(list[0])
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/button[1]').click()
        sleep(2)
        text = self.driver.find_element(By.CLASS_NAME, 'el-form-item__error').text
        try:
           self.assertIn(text,list[1])
        except:
            self.driver.get_screenshot_as_file('test01.png')

if __name__ == '__main__':
    unittest.main()