from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    home_page_input_username_loc = (By.NAME, "username")
    home_page_input_password_loc = (By.NAME, "password")
    home_page_button_login_loc = (By.CSS_SELECTOR, ".fastlg_l button")

    text_search=(By.CSS_SELECTOR,"td .xg1")
    text_search_btn=(By.CSS_SELECTOR,".scbar_btn_td .pn")

    haotest_link=(By.CSS_SELECTOR,".pbw:first-of-type h3 a strong")

    haotest_title=(By.CSS_SELECTOR,"#thread_subject")

    quit_btn = (By.CSS_SELECTOR,"#um > p:nth-child(2) > a:nth-child(18)")


    def login(self, name,pwd):
        # self.open_url("http://www.baidu.com")
        self.sendkeys(name, *self.home_page_input_username_loc)
        self.sendkeys(pwd, *self.home_page_input_password_loc)
        time.sleep(3)
        self.click(*self.home_page_button_login_loc)
    def search_text(self,title_search_text):
        self.clear(*self.text_search)
        self.sendkeys(title_search_text,*self.text_search)
        self.driver.implicitly_wait(5)
        self.click(*self.text_search_btn)
        self.switch_to_windows(1)
        self.click(*self.haotest_link)
        self.switch_to_windows(2)
    def find_haotest(self):
        return self.find_text(*self.haotest_title)

    # def find_haotest(self):
    #     t=self.find_element(*self.haotest_title)
    #     t1=t.text
    #     return t1

    def quit_loginer(self):
        self.click(*self.quit_btn)
