from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class selectService:
    
     def __init__(self):
         self.driver = webdriver.Chrome('chromedriver.exe')
         self.wait = WebDriverWait(self.driver, 10)
         self.driver.maximize_window()
         
     def open_browser(self, url, type=By.XPATH, value=''):
           self.driver.implicitly_wait(10)  
           self.driver.get(url)   
           element = self.driver.find_element(type, value)
           #implicitly_wait() 函數創建一個隱式等待，它將等待 10 秒鐘，直到頁面上的所有元素都載入完成。
           #如果在等待期間找到了需要的元素，Selenium 將立即繼
           #id='colophon' 是footer的元件，如果footer顯示了，就認定是完成

     def find_element(self, type=By.XPATH, value=''):
          self.wait.until(EC.presence_of_element_located((type, value)))
          return self.driver.find_element(type, value)
     
     def check_element_click(self, type=By.XPATH, value=''):
          self.wait = WebDriverWait(self.driver, 30)
          element = self.wait.until(EC.element_to_be_clickable((type, value)))
     
     def quit_driver(self):
          self.driver.quit()
     