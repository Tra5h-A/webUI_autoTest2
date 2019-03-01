import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import HomePage
import time
class DiscuzLogin(BaseTestCase):
    def test_discuz_login(self):
        home_page=HomePage(self.driver)
        home_page.login("admin", "bin19961013")
        t = home_page.find_user()
        self.assertEqual(t, "admin", msg=t)
        home_page.delete_new()
        home_page.glmk_add(3,"版块_3")
        home_page.quit_managerlogin()
        home_page.login("bin1192029250", "bin19961013")
        t1 = home_page.find_user()
        self.assertEqual(t1, "bin1192029250", msg=t1)
        home_page.newbk_send("普通用户发帖","普通用户的发帖内容")
        time.sleep(15)
        home_page.newbk_reply("普通用户回帖")
if __name__=="__main__":
    unittest.main()