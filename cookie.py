from selenium import webdriver
import time
class Cookie:
    def __init__ (self):
        self.link = "https://orteil.dashnet.org/cookieclicker/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def open(self):
        self.driver.get(self.link)
        time.sleep(2)
    def lang(self):
        self.driver.find_element("xpath", '//*[@id=\"langSelect-EN\"]').click()
        time.sleep(2)
    def coo(self):
        self.driver.find_element("id", "bigCookie").click()
    def tear_down(self):
        self.driver.execute()
cookie = Cookie()
cookie.open()
cookie.lang()
a = 0
while a < 1000:
    cookie.coo()
cookie.tear_down()