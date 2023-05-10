from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class selectService:
    
      def __init__(self):
         self.driver = webdriver.Chrome('chromedriver.exe')
         self.wait = WebDriverWait(self.driver, 10)
         self.driver.maximize_window()
         
      def open_browser(self, url):
           self.driver.get(url)

      def find_element(self, type=By.XPATH, value=''):
          return self.wait.until(EC.presence_of_element_located((type, value)))
     
      def check_element_click(self, type=By.XPATH, value=''):
          self.wait = WebDriverWait(self.driver, 30)
          return self.wait.until(EC.element_to_be_clickable((type, value)))
     
      def quit_driver(self):
          self.driver.quit()
     