# 封装unittest框架中的Setup（添加5秒的智能等待和浏览器窗口最大化）和tearDown（退出浏览器）等方法；
import unittest

from driver.driver import ChromeTest


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = ChromeTest()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.quit()