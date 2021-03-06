# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

links_landing_titles = {
    "Basic Skills Initiative" : r'Basic Skills Initiative',
    "Bio/Health Division" : r'Biological, Health and Environmental Sciences',
    "Biology Department" : r'Biology',
    "Bookstore" : r'De Anza College Bookstore',
    "Business, Computer Science and Applied Technologies" : r'Business/Computer Systems',
    "Business Department" : 'Business',
    }

class deAnzaIndex(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/directory/dir-az.html"
        self.verificationErrors = []
    
    def test_sauce_labs_headers(self):
        driver = self.driver

        for link in links_landing_titles:
            driver.get(self.base_url)
            driver.find_element_by_link_text(link).click()
            expected_title = links_landing_titles[link]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
