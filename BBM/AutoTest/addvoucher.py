import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

username='ADMIN'
access_key=''

     
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        
    def tearDown(self):
        self.driver.quit()
        
    def test_unit_add_voucher(self):
        print('bat dau')
        driver=self.driver
        driver.get("http://127.0.0.1:8000/voucher")
        inputVoucher=driver.find_element(By.NAME,value="voucher")
        inputVoucher.send_keys("huyleduc")
        time.sleep(1)
        
        selectCourt=Select(driver.find_element(By.NAME,"court"))
        selectCourt.select_by_visible_text("MC1 CL")
        time.sleep(1)
        
        percent=driver.find_element(By.NAME,value="percent")
        percent.clear()
        percent.send_keys("25")
        time.sleep(1)
        
        percent.send_keys(Keys.RETURN)
        time.sleep(10)
        
if __name__=="__main__":
    unittest.main()