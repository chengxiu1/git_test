# 封装截图、数据驱动读取等方法；
import csv
import os.path


def get_img(driver,phoneName):
     base_url = os.path.dirname(__file__)
     base_url = str(base_url)
     base_url = base_url.replace('\\','/')
     base = base_url.split('Website')[0]
     phone_url = base +'Website/test_report/srceenshot/' + phoneName
     driver.get_screenshot_as_file(phone_url)
def read(line):
     with open(r'C:\Users\Administrator\PycharmProjects\test\2024.6\9-11\EPR_PO\Website\test_data\test_csv.csv',encoding='utf-8')as f:
          data = csv.reader(f)
          for index,row in enumerate(data,1):
               if line == index:
                    return row