# 引入BasePage.py中封装好的方法，引入By方法类，封装登录用例页面元素位置和操作
# （使用CLASS_NAME方法封装用户名输入框，使用ID方法封装密码输入框、使用TAG_NAME方法封装登录按钮位置，封装输入用户名、密码、点击登录按钮等操作）；
from selenium.webdriver.common.by import By

from Website.test_case.page_object.BasePage import BasePage


class LoginPage(BasePage):
    wrl ='/'
    by_name = (By.CLASS_NAME,'')
    by_pwd = (By.ID,'')
    by_singin = (By.TAG_NAME,'')
    def find_by_name(self,name):
        self.find_element(*self.by_name).send_keys(name)
    def find_by_pwd(self,pwd):
        self.find_element(*self.by_pwd).send_keys(pwd)
    def find_by_singin(self):
        self.find_element(*self.by_singin).click()
def login_test(driver,name,pwd):
    test = LoginPage(driver)
    test.open()
    test.find_by_name(name)
    test.find_by_pwd(pwd)
    test.find_by_singin()