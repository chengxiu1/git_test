import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_denglu01(driver):
    driver.get('http://192.168.46.5:13077/login?redirect=%2Findex')
    driver.find_element(By.NAME, 'username').send_keys('XTGLY')
    driver.find_elements(By.CLASS_NAME, 'password')[0].send_keys('123456')
    driver.find_element(By.XPATH, '//*[@id="signIn"]').click()


def test_denglu02():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()

    driver.get('http://192.168.46.5:13077/login?redirect=%2Findex')
    driver.find_element(By.ID, 'username').send_keys('XTGLY')
    driver.find_element(By.CLASS_NAME, 'password').send_keys('123456')
    driver.find_element(By.TAG_NAME, 'button').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, '供应商信息1').click()
    sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr/td[6]/div/button[1]/span/a').click()
    sleep(2)
    all = driver.window_handles
    driver.switch_to.window(all[-1])
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button/i').click()
    driver.get_screenshot_as_file('2.png')

    driver.quit()


def test_denglu03():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()

    driver.get('http://192.168.46.5:13077/login?redirect=%2Find')
    driver.find_element(By.ID, 'username').send_keys('XTGLY')
    driver.find_element(By.CLASS_NAME, 'password').send_keys('123456')
    driver.find_element(By.TAG_NAME, 'button').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, '供应商信息').click()
    driver.quit()


if __name__ == '__main__':
    pytest.main()
