# 使用discover方法执行test_add.py测试用例并引入HTMLTestRunner方法生成html测试报告（测试报告title名为：Test Report，description内容为erp test）。
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

test_dir = 'test_add'
report_dir = 'test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
now = time.strftime('%H_%M_%S')
report_name = report_dir +'/'+now +'_result.html'
with open(report_name,'wb')as f:
    runner = HTMLTestRunner(stream=f,title='Test Report',description='erp test')
    runner.run(discover)
    f.close()