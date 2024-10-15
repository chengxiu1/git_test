# 引入unittest、ddt以及之前封装好的model，LoginPage，AddPage中的方法类，根据用例编写5条测试用例脚本，创建data参数来接收测试数据，并使用数据驱动输入用户名和密码（XTGLY/123456），
# 使用数据驱动输入商品单位名称，然后进行截图操作，最后对每一条测试用例进行assertIn断言操作，对比提示信息是否和预期一致；
from Website.test_case.model.function import read, get_img
from Website.test_case.model.myunit import StartEnd
from Website.test_case.page_object.AddPage import add_test, AddPage
from Website.test_case.page_object.LogingPage import login_test


class test_add(StartEnd):
    def teas01(self):
        data = read(2)
        login_test(self.driver,data[0],data[1])
        add_test(self.driver,data[2])
        get_img(self.driver,'test01.png')
        ass = AddPage(self.driver)
        self.assertIn(ass.find_text_success(),data[3])
    def teas02(self):
        data = read(3)
        login_test(self.driver,data[0],data[1])
        add_test(self.driver,data[2])
        get_img(self.driver,'test02.png')
        ass = AddPage(self.driver)
        self.assertIn(ass.find_text_float(),data[3])
    def teas03(self):
        data = read(4)
        login_test(self.driver,data[0],data[1])
        add_test(self.driver,data[2])
        get_img(self.driver,'test03.png')
        ass = AddPage(self.driver)
        self.assertIn(ass.find_text_float(),data[3])
    def teas04(self):
        data = read(5)
        login_test(self.driver,data[0],data[1])
        add_test(self.driver,data[2])
        get_img(self.driver,'test04.png')
        ass = AddPage(self.driver)
        self.assertIn(ass.find_text_float(),data[3])
    def teas05(self):
        data = read(6)
        login_test(self.driver,data[0],data[1])
        add_test(self.driver,data[2])
        get_img(self.driver,'test05.png')
        ass = AddPage(self.driver)
        self.assertIn(ass.find_text_float(),data[3])
