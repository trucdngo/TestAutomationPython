from selenium import webdriver
import os

class RunSafariTest():

    def run_safari(self):
        #download: selenium-server-standalone-3.8.1, & store it @ location below
        server_location = "/Users/trucngo/Documents/Selenium/selenium-server-standalone-3.8.1"
        os.environ["Selenium_Server"] = server_location
        driver = webdriver.Safari(quiet=True)
        driver.get("http://www.google.com")


ff = RunSafariTest()
ff.run_safari()