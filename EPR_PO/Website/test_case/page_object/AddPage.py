# 引入BasePage.py中封装好的方法，引入By方法类，封装好商品单位添加页面元素（使用LINK_TEXT方法封装商品单位按钮，使用CSS方法封装新增按钮，
# 使用XPATH方法封装商品单位名称输入框，使用CSS方法封装保存按钮，封装点击商品单位按钮、点击新增按钮、输入商品单位名称、点击保存按钮等操作），封装添加成功以及添加失败的提示信息文字；
from selenium.webdriver.common.by import By

from Website.test_case.page_object.BasePage import BasePage


class AddPage(BasePage):
    wrl ='/'
    by_spdw = (By.LINK_TEXT,'')
    by_add = (By.CSS_SELECTOR,'')
    by_input = (By.XPATH,'')
    by_baocun = (By.CSS_SELECTOR,'')
    text_success = (By.CLASS_NAME,'')
    text_float = (By.CLASS_NAME,'')
    def find_by_spdw(self):
        self.find_element(*self.by_spdw).click()
    def find_by_add(self):
        self.find_element(*self.by_add).click()
    def find_by_input(self,valuse):
        self.find_element(*self.by_input).send_keys(valuse)
    def find_by_baocun(self):
        self.find_element(*self.by_baocun).click()
    def find_text_success(self):
        return self.find_element(*self.text_success).text
    def find_text_float(self):
        return self.find_element(*self.text_float).text
def add_test(driver,valuse):
    test = AddPage(driver)
    test.find_by_spdw()
    test.find_by_add()
    test.find_by_input(valuse)
    test.find_by_baocun()