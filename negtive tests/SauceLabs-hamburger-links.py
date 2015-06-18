# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

all_css_locators = {
    'COMMUNITY' : ['a[title=\"Community\"]', 'Open Sauce'],
    'SOLUTIONS' : ['a[title=\"Solutions\"]', 'Selenium Testing'],
    'RESOURCES': ['a[title="Resources"]', 'Resources'],
    'ENTERPRISE': ['li.page.pull-left > a[title=\"Enterprise\"]', 'Enterprise'],
    'SIGN UP': ['a[title=\"Sign up\"]', 'Sign Up'],
    'DOCS': ['li.page.pull-left > a[title=\"Docs\"]', 'Docs'],
    'PRICING': ['li.page.pull-left > a[title=\"Pricing\"]', 'Pricing'],
    'LOGIN': ['a[title="Log in"]', 'Login'],
    }
    
all_xpaths_lacators = {
    'FEATURES' : ['(//a[contains(text(),"Features")])[3]', 'Features'],
    'COMPANY' : ['(//a[contains(text(),"Company")])[2]', 'Values'],
    }   
    
class saucelabsLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'https://saucelabs.com'
        self.verificationErrors = []    
        
        
    def test_saucelabs_links(self):
        driver = self.driver

        for name in all_css_locators:
            driver.get(self.base_url)
            driver.find_element_by_css_selector('a.hamburger').click()               
            driver.find_element_by_css_selector(all_css_locators[name][0]).click()            
            expected_title = all_css_locators[name][1]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e)) 
            
        for name in all_xpaths_lacators:
            driver.get(self.base_url)
            driver.find_element_by_css_selector('a.hamburger').click()    
            driver.find_element_by_xpath(all_xpaths_lacators[name][0]).click()            
            expected_title = all_xpaths_lacators[name][1]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()   
