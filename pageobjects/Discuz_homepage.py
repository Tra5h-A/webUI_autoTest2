from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
import random
class HomePage(BasePage):
    #1
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
    user=(By.CSS_SELECTOR,"#um > p:nth-child(2) > strong > a")

    quit_sys_btn=(By.LINK_TEXT,"退出")


##2

    duigou = (By.CSS_SELECTOR, "table tbody:nth-child(2) td:nth-child(2)")
    delete = (By.LINK_TEXT, "删除")
    yes_btn = (By.CSS_SELECTOR, ".o button")

    glzx_btn = (By.LINK_TEXT, "管理中心")
    luntan = (By.LINK_TEXT, "论坛")
    fid_up=(By.CSS_SELECTOR, ".tb tbody:nth-last-child(3) tr:nth-child(1) td:nth-child(2) input")
    fid = (By.CSS_SELECTOR, ".tb tbody:nth-last-child(2) tr:nth-child(1) td:nth-child(2) input")
    addbk_btn = (By.LINK_TEXT, "添加新版块")
    bkname = (By.CSS_SELECTOR, "tbody:nth-last-child(2)  tr:nth-last-child(2) td:last-of-type div input")
    submit_btn2 = (By.CSS_SELECTOR, "#submit_editsubmit")

    quit_btn = (By.XPATH, '//*[@id="frameuinfo"]/p[1]/a')
    ##

    new_bk = (By.CSS_SELECTOR, "tr:nth-last-child(2)  > td:nth-child(2) > h2 > a")
   #3


    text_search = (By.CSS_SELECTOR, "td .xg1")
    text_search_btn = (By.CSS_SELECTOR, ".scbar_btn_td .pn")

    haotest_link = (By.CSS_SELECTOR, ".pbw:first-of-type h3 a strong")

    haotest_title = (By.CSS_SELECTOR, "#thread_subject")

    # quit_btn = (By.LINK_TEXT, "退出")
    #4
    button_sendpiao = (By.LINK_TEXT, "发起投票")
    toupiao_title = (By.CSS_SELECTOR, ".pbt .z span .px")
    xuan1 = (By.CSS_SELECTOR, ".mbm p:first-of-type input")
    xuan2 = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    xuan3 = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")



    xuanxiang_1 = (By.CSS_SELECTOR, ".pcht tbody tr:first-of-type td:first-of-type")
    xuanxiang_2 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(3) td:first-of-type")
    xuanxiang_3 = (By.CSS_SELECTOR, ".pcht tbody tr:nth-child(5) td:first-of-type")

    submit_toupiao_btn = (By.CSS_SELECTOR, "#pollsubmit")

    xuan1_name = (By.CSS_SELECTOR, "tr:nth-child(1) > td.pvt > label")
    xuan2_name = (By.CSS_SELECTOR, "tr:nth-child(3) > td.pvt > label")
    xuan3_name = (By.CSS_SELECTOR, "tr:nth-child(5) > td.pvt > label")
    xuan1_per = (By.XPATH, '//*[@id="poll"]/div[2]/table/tbody/tr[2]/td[2]')
    xuan2_per = (By.XPATH, '//*[@id="poll"]/div[2]/table/tbody/tr[4]/td[2]')
    xuan3_per = (By.XPATH, '//*[@id="poll"]/div[2]/table/tbody/tr[6]/td[2]')
    tou_title = (By.CSS_SELECTOR, "#thread_subject")

    def login(self, name,pwd):
        # self.open_url("http://www.baidu.com")
        self.sendkeys(name, *self.home_page_input_username_loc)
        self.sendkeys(pwd, *self.home_page_input_password_loc)
        # time.sleep(3)
        self.click(*self.home_page_button_login_loc)
        time.sleep(3)
    # def assert_Equal_login(self,ac,ex):
    #     self.assert_Equal(ac,ex)
    def find_user(self):
        return self.find_text(*self.user)
    def send_new(self,title,text1):
        # time.sleep(3)
        self.click(*self.button_moren_loc)
        self.click(*self.button_send_loc)
        # time.sleep(2)
        self.sendkeys(title,*self.title_send_loc)
        # time.sleep(3)
        self.switch_to_frame(0)
        # time.sleep(3)
        self.sendkeys(text1,*self.text_box)
        self.switch_to_current_window()
        self.click(*self.submit_btn)
        # time.sleep(3)
    def reply_new(self,text2):
        self.click(*self.button_reply_loc)
        time.sleep(2)
        self.sendkeys(text2,*self.reply_box_loc)
        # time.sleep(1)
        self.click(*self.reply_btn_loc)
        # time.sleep(3)

    def quit_loginer(self):
        self.click(*self.quit_sys_btn)
        time.sleep(3)
    # def assert_True_quit(self):
    #     self.assert_True(*self.home_page_button_login_loc)
    #2
    def delete_new(self):
        # time.sleep(3)
        self.click(*self.button_moren_loc)
        # time.sleep(5)
        self.click(*self.duigou)
        self.click(*self.delete)
        # time.sleep(1)
        self.click(*self.yes_btn)
    def glmk_add(self,num,text1):
        self.click(*self.glzx_btn)
        self.switch_to_windows(1)
        # time.sleep(5)
        self.click(*self.luntan)
        # time.sleep(5)
        self.switch_to_frame(0)
        # time.sleep(5)
        self.click(*self.addbk_btn)
        # time.sleep(1)
        # self.clear(self.bkname)
        self.sendkeys(num, *self.fid)
        self.sendkeys(text1,*self.bkname)
        # time.sleep(3)
        self.click(*self.submit_btn2)
        # time.sleep(5)
    def quit_managerlogin(self):
        self.switch_to_current_window()
        self.click(*self.quit_btn)
        self.click(*self.quit_sys_btn)
    def newbk_send(self,title,text2):
        # time.sleep(3)
        self.click(*self.new_bk)
        self.switch_to_current_window()
        self.click(*self.button_send_loc)
        # time.sleep(2)
        self.sendkeys(title, *self.title_send_loc)
        # time.sleep(3)
        self.switch_to_frame(0)
        # time.sleep(3)
        self.sendkeys(text2, *self.text_box)
        self.switch_to_current_window()
        self.click(*self.submit_btn)
    def newbk_reply(self,text3):
        self.click(*self.button_reply_loc)
        # time.sleep(2)
        self.sendkeys(text3, *self.reply_box_loc)
        # time.sleep(1)
        self.click(*self.reply_btn_loc)
        # time.sleep(3)
    #3


    def search_text(self, title_search_text):
        self.clear(*self.text_search)
        self.sendkeys(title_search_text, *self.text_search)
        self.click(*self.text_search_btn)
        self.switch_to_windows(1)
        self.click(*self.haotest_link)
        self.switch_to_windows(2)
    def find_haotest(self):
        return self.find_text(*self.haotest_title)

    #4
    def new_toupiao(self,title,x1,x2,x3):
        # time.sleep(1)
        self.click(*self.button_moren_loc)
        # time.sleep(1)
        self.click(*self.button_send_loc)
        # time.sleep(1)
        self.click(*self.button_sendpiao)
        # time.sleep(2)
        self.sendkeys(title,*self.toupiao_title)
        # time.sleep(2)
        self.sendkeys(x1,*self.xuan1)
        self.sendkeys(x2, *self.xuan2)
        self.sendkeys(x3, *self.xuan3)
        # time.sleep(5)
        self.click(*self.submit_btn)
        # time.sleep(5)
    def toupiao(self):
        num=random.randint(1,3)
        if num==1:
            self.click(*self.xuanxiang_1)
        elif num==2:
            self.click(*self.xuanxiang_2)
        else:
            self.click(*self.xuanxiang_3)
        # time.sleep(1)
        self.click(*self.submit_toupiao_btn)
    def persent(self):
        x1=self.find_text(*self.xuan1_name)
        x_1=self.find_text(*self.xuan1_per)
        x2 =self.find_text(*self.xuan2_name)
        x_2=self.find_text(*self.xuan2_per)
        x3 =self.find_text(*self.xuan3_name)
        x_3=self.find_text(*self.xuan3_per)
        print(x1,x_1,"\n",x2,x_2,"\n",x3,x_3)
