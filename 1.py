from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://kuwo.cn/')
driver.implicitly_wait(3)
driver.maximize_window()
