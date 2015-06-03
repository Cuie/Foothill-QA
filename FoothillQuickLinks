# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

dropdown_items = {
    "A-Z Site Index" : "Site A - Z Index",
    "Bookstore" : "Home",
    "Calendar" : "Calendar & News",
    "English" : "Foothill College Language Arts Staff Resources",
    }
    
class FoothillQuickLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.base_url = "http://www.foothill.edu/"
        self.verificationErrors = []

    def test_foothill_quick_links(self):
        driver = self.driver

        for dropdown_item in dropdown_items:
            driver.get(self.base_url)
            quick_list = driver.find_element_by_css_selector("select[name=\"topnav\"]")
            Select(quick_list).select_by_visible_text(dropdown_item)
            expected_title = dropdown_items[dropdown_item]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))    
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()        
