import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class TestPIM(unittest.TestCase): 
    
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_search_user_by_suggestion_name(self): 
        # ARRANGE
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys('Admin')
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys('admin123')
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()
        #wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '//button[@class="oxd-icon-button"]'))).click()
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@class="oxd-input oxd-input--active"]'))).send_keys('Aaliyah')
     
        sleep(20)
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//div[@role="listbox"])[1]'))).click()
        sleep(2)
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()
        check_first_name_user = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="oxd-table-card-cell"])[2]/div[2]'))).text
        check_id_user = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="oxd-table-card-cell"])[1]/div[2]'))).text

        self.assertIn('Aaliyah', check_first_name_user)
        self.assertEqual(check_id_user, '0038')
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()