from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
import random
class HomePage(BasePage):
    home_page_input_username_loc = (By.NAME, "username")
    home_page_input_password_loc = (By.NAME, "password")
    home_page_button_login_loc = (By.CSS_SELECTOR, ".fastlg_l button")

    button_moren_loc = (By.LINK_TEXT, "默认版块")
    button_send_loc = (By.ID, "newspecial")
    button_sendpiao=(By.LINK_TEXT,"发起投票")
    toupiao_title=(By.CSS_SELECTOR,".pbt .z span .px")
    xuan1=(By.CSS_SELECTOR,".mbm p:first-of-type input")
    xuan2 = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    xuan3 = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")

    submit_btn = (By.ID, "postsubmit")

    xuanxiang_1=(By.CSS_SELECTOR,".pcht tbody tr:first-of-type td:first-of-type")
    xuanxiang_2 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3) td:first-of-type")
    xuanxiang_3 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5) td:first-of-type")

    submit_toupiao_btn=(By.CSS_SELECTOR,"#pollsubmit")

    xuan1_name=(By.CSS_SELECTOR,"tr:nth-child(1) > td.pvt > label")
    xuan2_name=(By.CSS_SELECTOR,"tr:nth-child(3) > td.pvt > label")
    xuan3_name = (By.CSS_SELECTOR, "tr:nth-child(5) > td.pvt > label")
    xuan1_per=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[2]/td[2]')
    xuan2_per=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[4]/td[2]')
    xuan3_per=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[6]/td[2]')
    tou_title=(By.CSS_SELECTOR,"#thread_subject")
    def login(self, name,pwd):
        # self.open_url("http://www.baidu.com")
        self.sendkeys(name, *self.home_page_input_username_loc)
        self.sendkeys(pwd, *self.home_page_input_password_loc)
        time.sleep(3)
        self.click(*self.home_page_button_login_loc)
    def new_toupiao(self,title,x1,x2,x3):
        time.sleep(1)
        self.click(*self.button_moren_loc)
        time.sleep(1)
        self.click(*self.button_send_loc)
        time.sleep(1)
        self.click(*self.button_sendpiao)
        time.sleep(2)
        self.sendkeys(title,*self.toupiao_title)
        time.sleep(2)
        self.sendkeys(x1,*self.xuan1)
        self.sendkeys(x2, *self.xuan2)
        self.sendkeys(x3, *self.xuan3)
        time.sleep(5)
        self.click(*self.submit_btn)
        time.sleep(5)
    def toupiao(self):
        num=random.randint(1,3)
        if num==1:
            self.click(*self.xuanxiang_1)
        elif num==2:
            self.click(*self.xuanxiang_2)
        else:
            self.click(*self.xuanxiang_3)
        time.sleep(1)
        self.click(*self.submit_toupiao_btn)
    def persent(self):
        x1=self.find_text(*self.xuan1_name)
        x_1=self.find_text(*self.xuan1_per)
        x2 =self.find_text(*self.xuan2_name)
        x_2=self.find_text(*self.xuan2_per)
        x3 =self.find_text(*self.xuan3_name)
        x_3=self.find_text(*self.xuan3_per)

        print(x1,x_1,"\n",x2,x_2,"\n",x3,x_3)

