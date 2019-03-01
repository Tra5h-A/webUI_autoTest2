import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import HomePage


class DiscuzLogin(BaseTestCase):
    def test_discuz_login(self):
        home_page=HomePage(self.driver)
        home_page.login("admin", "bin19961013")
        t = home_page.find_user()
        self.assertEqual(t, "admin", msg=t)
        home_page.new_toupiao("测试投票","选项1","选项2","选项3")
        home_page.toupiao()
        home_page.persent()

if __name__=="__main__":
    unittest.main()