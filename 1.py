from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get('http://192.168.46.5:13077/login?redirect=%2Findex')
driver.find_element(By.ID,'username').send_keys('XTGLY')
driver.find_elements(By.TAG_NAME,'input')[1].send_keys('123456')
driver.find_element(By.CLASS_NAME,'primary').click()
sleep(2)
driver.find_elements(By.TAG_NAME,'button')[3].click()
sleep(2)
Select1 = driver.find_element(By.ID,'select_add_class_bug')
Select(Select1).select_by_value('1')
sleep(2)
Select2 = driver.find_elements(By.TAG_NAME,'select')[3]
Select(Select2).select_by_visible_text('测试')
sleep(2)
driver.get_screenshot_as_file("D:test_Select01.png")