import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import HomePage
import time
class DiscuzLogin(BaseTestCase):
    def test_discuz_login(self):
        home_page=HomePage(self.driver)
        home_page.login("admin", "bin19961013")
        home_page.search_text("haotest")
        # home_page.find_haotest()
        t=home_page.find_haotest()
        self.assertEqual(t,"haotest",msg=t)
        time.sleep(1)
        home_page.quit_loginer()
        time.sleep(5)
if __name__=="__main__":
    unittest.main()