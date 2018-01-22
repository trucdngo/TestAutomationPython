
from selenium import webdriver
import os

class RunChromeTest():

    def run_chrome(self):
        driverLocation = "/Users/trucngo/Documents/Selenium/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.cnn.com")


ff = RunChromeTest()
ff.run_chrome()