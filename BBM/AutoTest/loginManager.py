import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

username='ADMIN'
access_key=''

     
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def tearDown(self):
        self.driver.close()
        
      # TH3 : ten dang nhap d, mat khau s  
      # TH2 : ten dang nhap s, mat khau d 
      # TH1 : ca 2 dung
      # TH4 : khong nhap gi 
        
    def test_unit_login_manager_1(self):
        print('bat dau')
        driver=self.driver
        driver.get("http://127.0.0.1:8000/login/")
        inputUserName=driver.find_element(By.NAME,value="username")
        inputUserName.send_keys("hoangrole3")
        time.sleep(2.5)
        
        password=driver.find_element(By.NAME,value="password")
        password.send_keys("1")
        
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # actualTitle=driver.title
        # print(actualTitle)
        
        # assert(actualTitle=="BBM Quản Lý")
        
    def test_unit_login_manager_2(self):
        print('bat dau')
        driver=self.driver
        driver.get("http://127.0.0.1:8000/login/")
        inputUserName=driver.find_element(By.NAME,value="username")
        inputUserName.send_keys("hoangrole33")
        time.sleep(2.5)
        
        password=driver.find_element(By.NAME,value="password")
        password.send_keys("1")
        
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # actualTitle=driver.title
        # print(actualTitle)
        
        # assert(actualTitle=="BBM Quản Lý")
    
    def test_unit_login_manager_3(self):
        print('bat dau')
        driver=self.driver
        driver.get("http://127.0.0.1:8000/login/")
        inputUserName=driver.find_element(By.NAME,value="username")
        inputUserName.send_keys("hoangrole3")
        time.sleep(2.5)
        
        password=driver.find_element(By.NAME,value="password")
        password.send_keys("2")
        
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # actualTitle=driver.title
        # print(actualTitle)
        
        # assert(actualTitle=="BBM Quản Lý")
        
    def test_unit_login_manager_4(self):
        print('bat dau')
        driver=self.driver
        driver.get("http://127.0.0.1:8000/login/")
        inputUserName=driver.find_element(By.NAME,value="username")
        inputUserName.send_keys("")
        time.sleep(2.5)
        
        password=driver.find_element(By.NAME,value="password")
        password.send_keys("")
        
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # actualTitle=driver.title
        # print(actualTitle)
        
        # assert(actualTitle=="BBM Quản Lý")    
if __name__=="__main__":
    unittest.main()