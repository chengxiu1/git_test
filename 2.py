import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
class denlu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.close()
    def test_denglu01(self):
        self.driver.get('192.168.46.5:16097')
        self.driver.find_element(By.NAME, 'username').send_keys('XTGLY')
        self.driver.find_elements(By.CLASS_NAME, 'password')[0].send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="signIn"]').click()
    def test_denglu02(self):
        self.driver.get('192.168.46.5:16097')
        self.driver.find_element(By.ID, 'username').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, 'password').send_keys('123456')
        self.driver.find_element(By.CLASS_NAME, 'primary ').click()
        self.driver.find_element(By.LINK_TEXT, '供应商信息').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/button[2]').click()
        all = self.driver.window_handles
        self.driver.switch_to.window(all[-1])
        self.driver.find_element(By.XPATH, '').click()
        self.driver.get_screenshot_as_file('test01.png')
if __name__ == '__main__':
    unittest.main()