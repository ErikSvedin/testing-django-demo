# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_is_correct_title(self):
        # Visit app
        self.browser.get('http://127.0.0.1:8000')

        # Expect webpage to be about drone
        self.assertIn('Webpage about drone', self.browser.title)


if __name__ == '__main__':
    unittest.main()
