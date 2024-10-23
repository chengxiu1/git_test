import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
class denlu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.quit()
    def test_denglu01(self):
        self.driver.get('http://192.168.46.5:13077/login?redirect=%2Findex')
        self.driver.find_element(By.NAME,'username').send_keys('XTGLY')
        self.driver.find_elements(By.CLASS_NAME,'password')[0].send_keys('123456')
        self.driver.find_element(By.XPATH,'//*[@id="signIn"]').click()
    def test_denglu02(self):
        self.driver.get('http://192.168.46.5:13077/login?redirect=%2Findex')
        self.driver.find_element(By.ID, 'username').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, 'password').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, '供应商信息').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr/td[6]/div/button[1]/span/a').click()
        sleep(2)
        all = self.driver.window_handles
        self.driver.switch_to.window(all[-1])
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button/i').click()
        self.driver.get_screenshot_as_file('2.png')

    def test_denglu03(self):
        self.driver.get('http://192.168.46.5:13077/login?redirect=%2Findex')
        self.driver.find_element(By.ID, 'username').send_keys('XTGLY')
        self.driver.find_element(By.CLASS_NAME, 'password').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, '供应商信息').click()
        sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr/td[6]/div/button[1]/span/a').click()
        sleep(2)
        all = self.driver.window_handles
        self.driver.switch_to.window(all[-1])
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button/i').click()
        self.driver.get_screenshot_as_file('2.png')
if __name__ == '__main__':
    unittest.main()