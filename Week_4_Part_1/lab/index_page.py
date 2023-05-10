from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageBase import PageBase


class IndexPage(PageBase):

     def click_add_to_cart(self, prdouct_name):
         locator = (By.XPATH, f"//h2[text()='{prdouct_name}']/ancestor::li/a[text()='Add to cart']")
         element = self.find_element(locator, clickable=True)
         element.click()

     def click_view_cart(self, prdouct_name):
         locator = (By.XPATH, f"//h2[text()='{prdouct_name}']/ancestor::li/a[@title='View cart']")
         element = self.find_element(locator, clickable=True)
         element.click()

     def qty_text_field(self, prdouct_name, qty):
         locator = (By.XPATH, f"//a[text()='{prdouct_name}']/ancestor::tr/descendant::input[@title='Qty']")
         element = self.find_element(locator, clickable=False)
         element.clear()
         element.send_keys(qty)

     def update_cart_btn(self, value):
         locator = (By.XPATH, f"//button[text()='{value}']")
         element = self.find_element(locator, clickable=True)
         element.click()
         locator = (By.XPATH, f"//button[text()='{value}' and @aria-disabled='true']")        
         element = self.find_element_unclickable(locator) 

     def unit_price(self, prdouct_name):
         locator = (By.XPATH, f"//a[text()='{prdouct_name}']/ancestor::tr/descendant::span[contains(@class, 'amount')]/bdi")
         element = self.find_element(locator, clickable=False)
         return element.text
   
     def subtotal_text(self, value):
         locator = (By.XPATH, f"//td[@data-title='{value}']/descendant::bdi")
         element = self.find_element(locator, clickable=False)       
         return element.text 
