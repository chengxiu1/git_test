# 封装selenium的基础操作类方法（get、find_element等）；
class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.url = ''
    def _open(self,url_):
        _url = self.url + url_
        self.driver.get(_url)
    def open(self):
        return self._open(self.url)
    def find_element(self,*line):
        self.driver.find_element(*line)