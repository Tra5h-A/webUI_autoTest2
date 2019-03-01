from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage(BasePage):
    home_page_input_username_loc = (By.NAME, "username")
    home_page_input_password_loc = (By.NAME, "password")
    home_page_button_login_loc = (By.CSS_SELECTOR, ".fastlg_l button")

    button_moren_loc = (By.LINK_TEXT, "默认版块")
    duigou=(By.CSS_SELECTOR,"table tbody:nth-child(2) td:nth-child(2)")
    delete = (By.LINK_TEXT,"删除")
    yes_btn=(By.CSS_SELECTOR,".o button")

    glzx_btn=(By.LINK_TEXT,"管理中心")
    luntan=(By.LINK_TEXT,"论坛")
    fid=(By.CSS_SELECTOR,"#group_1 tr:nth-child(2) > td:nth-child(2) > input")
    addbk_btn=(By.LINK_TEXT,"添加新版块")
    bkname=(By.CSS_SELECTOR,"tbody:nth-last-child(2)  tr:nth-last-child(2) td:last-of-type div input")
    submit_btn2=(By.CSS_SELECTOR,"#submit_editsubmit")

    quit_btn=(By.XPATH,'//*[@id="frameuinfo"]/p[1]/a')
    quit_sys_btn=(By.LINK_TEXT,"退出")

    new_bk=(By.CSS_SELECTOR,"tr:nth-last-child(2)  > td:nth-child(2) > h2 > a")
    button_send_loc = (By.ID, "newspecial")
    title_send_loc = (By.ID, "subject")
    text_box = (By.CSS_SELECTOR, "html body")
    submit_btn = (By.ID, "postsubmit")

    button_reply_loc = (By.ID, "post_reply")
    reply_box_loc = (By.CSS_SELECTOR, "div>textarea")
    reply_btn_loc = (By.CSS_SELECTOR, "div>button")

    def login(self, name,pwd):
        # self.open_url("http://www.baidu.com")
        self.sendkeys(name, *self.home_page_input_username_loc)
        self.sendkeys(pwd, *self.home_page_input_password_loc)
        time.sleep(3)
        self.click(*self.home_page_button_login_loc)
    def delete_new(self):
        time.sleep(3)
        self.click(*self.button_moren_loc)
        time.sleep(5)
        self.click(*self.duigou)
        self.click(*self.delete)
        time.sleep(1)
        self.click(*self.yes_btn)
    def glmk_add(self,num,text1):
        self.click(*self.glzx_btn)
        self.switch_to_windows(1)
        time.sleep(5)
        self.click(*self.luntan)
        time.sleep(5)
        self.switch_to_frame(0)
        time.sleep(5)
        self.click(*self.addbk_btn)
        time.sleep(1)
        # self.clear(self.bkname)
        self.sendkeys(num,*self.fid)
        self.sendkeys(text1,*self.bkname)
        time.sleep(3)
        self.click(*self.submit_btn2)
        time.sleep(5)
    def quit_managerlogin(self):
        self.switch_to_current_window()
        self.click(*self.quit_btn)
        self.click(*self.quit_sys_btn)
    def newbk_send(self,title,text2):
        time.sleep(3)
        self.click(*self.new_bk)
        self.switch_to_current_window()
        self.click(*self.button_send_loc)
        time.sleep(2)
        self.sendkeys(title, *self.title_send_loc)
        time.sleep(3)
        self.switch_to_frame(0)
        time.sleep(3)
        self.sendkeys(text2, *self.text_box)
        self.switch_to_current_window()
        self.click(*self.submit_btn)
    def newbk_reply(self,text3):
        self.click(*self.button_reply_loc)
        time.sleep(2)
        self.sendkeys(text3, *self.reply_box_loc)
        time.sleep(1)
        self.click(*self.reply_btn_loc)
        time.sleep(3)


