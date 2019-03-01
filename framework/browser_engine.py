#_*_ coding:utf-8_*_
import os.path
from configparser import ConfigParser
from  selenium import  webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    chrome_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir+'/tools/IEDriverServer.exe'
    firefox_driver_path=dir+"/tools/geckodriver.exe"

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath("."))+'/config/config.ini'
        config.read(file_path)

        browser=config.get("browserType","browserName")
        logger.info("You had select %s browser."%browser)
        url=config.get("testServer","URL")
        logger.info("The test server url is:%s"%url)
        if browser=="Firefox":
            driver=webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser=="Chrome":
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser=="IE":
            driver=webdriver.Ie(self.ie_driver_path)
            logger.info("Starting Ie browser.")

        driver.get(url)
        logger.info("Open url:%s"%url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()
