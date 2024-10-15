import unittest
from csvv import read
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
@ddt.ddt
class denlu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.quit()
    @ddt.data(*read)
    def test_denglu01(self,list):
        self.driver.get('192.168.46.5:16097')
        self.driver.find_element(By.ID, 'username').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, 'password').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, 'button ').click()
        self.driver.find_element(By.LINK_TEXT, '商品分类').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/button').click()
        self.driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys(list[0])
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/button[1]').click()
        ass = self.driver.find_element(By.LINK_TEXT, '商品分类名称必填，请重新输入。').text
        try:
            self.assertEqual(ass,list[1])
        except:
            self.driver.get_screenshot_as_file('test01.png')
if __name__ == '__main__':
    unittest.main()