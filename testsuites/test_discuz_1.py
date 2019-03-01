import unittest

from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import HomePage
import time
class DiscuzLogin(BaseTestCase):
    def test_discuz_login(self):
        home_page=HomePage(self.driver)
        home_page.login("admin","bin19961013")
        t=home_page.find_user()
        # print(t)
        # home_page.assert_Equal_login(t,"admin")
        self.assertEqual(t,"admin",msg=t)
        home_page.send_new("haotest","这是一个测试帖")
        time.sleep(5)
        home_page.reply_new("回复测试帖")
        home_page.quit_loginer()
        self.assertTrue(home_page.home_page_button_login_loc)
        # home_page.assert_True_quit()
if __name__=="__main__":
    unittest.main()