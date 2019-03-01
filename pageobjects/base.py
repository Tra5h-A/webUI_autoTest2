from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os.path
import time

logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):  #浏览器后退按钮
        self.driver.back()
        logger.info("点击后退，返回页面.")
    def forward(self):  #浏览器前进按钮
        self.driver.forward()
        logger.info("点击前进，返回页面.")
    def open_url(self,url):  #打开连接
        self.driver.get(url)
    def quit_browser(self):#关闭并停止浏览器服务
        self.driver.quit()
    def close(self):  #关闭链接
        try:
            self.driver.close()
            logger.info("关闭当前窗口.")
        except Exception as e:
            self.get_windows_img()
            logger.error("关闭当前窗口失败： %s"%e)
    def find_element(self,*loc): #查找页面元素
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("%s找到页面元素-->%s"%(self,loc))
            return self.driver.find_element(*loc)

        except:
            self.get_windows_img()
            logger.error("%s页面中未能找到%s元素"%(self,loc))
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+'/screenshots/'
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("已截图并保存到文件夹:/screenshots")
        except Exception as e:
            self.get_windows_img()
            self.get_windows_img()
            logger.error("截图失败!：%s"%e )
    def sendkeys(self,text,*loc):  #输入
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容:%s"%text)
        except Exception as e:
            self.get_windows_img()
            logger.error("输入内容失败： %s" %e)
            self.get_windows_img()
    def clear(self,*loc):  #清除文本框
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("清除文本框")
        except Exception as e:
            self.get_windows_img()
            logger.error("清除文本框失败： %s"%e)
    def click(self,*loc): #点击元素
        try:
            el = self.find_element(*loc)
            el.click()
            logger.info("元素 %s 被点击."%(el.text))
        except Exception as e:
            self.get_windows_img()
            logger.error("点击元素失败： %s"%e)
    def switch_to_frame(self,n):
        iframe = self.driver.find_elements_by_tag_name("iframe")[n]
        self.driver.switch_to.frame(iframe)
    def switch_to_current_window(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def switch_to_windows(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])
    def find_text(self,*loc):
        t=self.find_element(*loc)
        t1=t.text
        return t1
    # def assert_Equal(self,actual,expect):
    #     try:
    #         unittest.TestCase.assertEqual(actual, expect, msg=actual)
    #         logger.info("断言！")
    #     finally:
    #         self.get_windows_img()
    # def assert_True(self,*loc):
    #     el=self.find_element(*loc)
    #     try:
    #         unittest.TestCase.assertTrue(el)
    #         logger.info("断言！")
    #     finally:
    #         self.get_windows_img()