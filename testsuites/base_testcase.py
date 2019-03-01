import unittest
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser=BrowserEngine()
        self.driver=browser.open_browser()
        print("开始进行测试")
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()
        print("测试结束")