import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from flask import Flask

server = os.getenv("SERVER")

class rootText(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor = "http://localhost:4444/wd/hub",
            desired_capabilities = {"browserName": "chrome", "javascriptEnabled": True}
            )

    def test_find_hello_world(self):
        driver = self.driver
        driver.get("http://{}:5000".format(server))
        bodyText = self.driver.find_element_by_tag_name('body').text
        print(bodyText)
        self.assertTrue("Hello, World!" in bodyText, "Missing expected text.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()