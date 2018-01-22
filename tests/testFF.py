
from selenium import webdriver
driver = webdriver.Firefox()


class RunFFTest():

    def run_firefox(self):
        driver.get("http://www.cnn.com")

ff = RunFFTest()
ff.run_firefox()
