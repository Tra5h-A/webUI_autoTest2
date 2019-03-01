from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage(BasePage):
    home_page_input_username_loc = (By.NAME, "username")
    home_page_input_password_loc = (By.NAME, "password")
    home_page_button_login_loc = (By.CSS_SELECTOR, ".fastlg_l button")

    button_moren_loc=(By.LINK_TEXT,"默认版块")
    button_send_loc=(By.ID,"newspecial")
    title_send_loc=(By.ID,"subject")
    # iframe1=(By.TAG_NAME,"iframe")[0]
    text_box=(By.CSS_SELECTOR,"html body")
    submit_btn=(By.ID,"postsubmit")

    button_reply_loc=(By.ID,"post_reply")
    reply_box_loc=(By.CSS_SELECTOR,"div>textarea")
    reply_btn_loc=(By.CSS_SELECTOR,"div>button")

    quit_btn=(By.LINK_TEXT,"退出")

    def login(self, name,pwd):
        # self.open_url("http://www.baidu.com")
        self.sendkeys(name, *self.home_page_input_username_loc)
        self.sendkeys(pwd, *self.home_page_input_password_loc)
        time.sleep(3)
        self.click(*self.home_page_button_login_loc)
    def send_new(self,title,text1):
        time.sleep(3)
        self.click(*self.button_moren_loc)
        self.click(*self.button_send_loc)
        time.sleep(2)
        self.sendkeys(title,*self.title_send_loc)
        time.sleep(3)
        self.switch_to_frame(0)
        time.sleep(3)
        self.sendkeys(text1,*self.text_box)
        self.switch_to_current_window()
        self.click(*self.submit_btn)
        time.sleep(3)
    def reply_new(self,text2):
        self.click(*self.button_reply_loc)
        time.sleep(2)
        self.sendkeys(text2,*self.reply_box_loc)
        time.sleep(1)
        self.click(*self.reply_btn_loc)
        time.sleep(3)
    def quit_loginer(self):
        self.click(*self.quit_btn)