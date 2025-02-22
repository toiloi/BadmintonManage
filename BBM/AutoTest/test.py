import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
inputUsername=driver.find_element(By.NAME,value="username")
print(inputUsername)
inputUsername.send_keys("admin")
time.sleep(2.5)

password=driver.find_element(By.NAME,value="password")
print(password)
password.send_keys("1")
time.sleep(2.5)

password.send_keys(Keys.RETURN)
time.sleep(10)