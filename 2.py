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
        self.driver.get('http://192.168.46.5:13077')
        self.driver.find_element(By.NAME, 'username').send_keys('XTGLY')
        self.driver.find_elements(By.CLASS_NAME, 'password')[0].send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="signIn"]').click()
    def test_denglu02(self):
        self.driver.get('http://192.168.46.5:13077')
        self.driver.find_element(By.ID, 'username').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, 'password').send_keys('123456')
        self.driver.find_element(By.CLASS_NAME, 'primary ').click()
if __name__ == '__main__':
    unittest.main()