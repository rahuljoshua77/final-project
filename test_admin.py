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
        
    def test_system_add_user(self): 
        # ARRANGE
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys('Admin')
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys('admin123')
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//li[@class="oxd-main-menu-item-wrapper"])[1]'))).click()
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'))).click()
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="oxd-select-wrapper"])[1]'))).click()   
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Admin")]'))).click()   
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="oxd-select-wrapper"])[2]'))).click()     
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Enabled")]'))).click()    
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Type for hints..."]'))).send_keys('Aaliyah')
        sleep(20)
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//div[@role="listbox"])[1]'))).click()
        sleep(2)
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]'))).send_keys('jokerssss')
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//input[@type="password"])[1]'))).send_keys('Testing123$$')
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '(//input[@type="password"])[2]'))).send_keys('Testing123$$')
        
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()
        check_success_add = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Successfully Saved")]'))).text
        self.assertIn('Successfully', check_success_add)
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()