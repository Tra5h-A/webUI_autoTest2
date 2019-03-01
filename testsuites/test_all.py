import sys
sys.path.append('E:/Discuz')
import HTMLTestRunner
import unittest
import os
from testsuites import test_discuz_1
from testsuites import test_discuz_2
from testsuites import test_discuz_3
from testsuites import test_discuz_4


# print(sys.path)
#设置报告文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
# print(cur_path)
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)
#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_discuz_1.DiscuzLogin))
suite.addTest(unittest.makeSuite(test_discuz_2.DiscuzLogin))
suite.addTest(unittest.makeSuite(test_discuz_3.DiscuzLogin))
suite.addTest(unittest.makeSuite(test_discuz_4.DiscuzLogin))

if __name__=="__main__":
    #打开一个文件，将result写入此file中
    html_report=report_path+ r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)