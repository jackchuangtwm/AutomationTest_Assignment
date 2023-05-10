from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from index_page import IndexPage

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


index_page = IndexPage(driver)

try:
      driver.maximize_window()
      driver.get("http://demostore.supersqa.com/")

      # Click Add To Cart - Album
      index_page.click_add_to_cart('Album')

      # Click view cart element
      index_page.click_view_cart('Album')
    
      # Change quantity to 2
      qty = 2
      index_page.qty_text_field('Album', qty)

      # Click Update Cart Button
      index_page.update_cart_btn('Update cart')

      # Get Unit Price Value
      unit_price_elem = index_page.unit_price('Album')

      # Get Subtotal Value
      subtotal_text_elem = index_page.subtotal_text('Subtotal')

      expect_subtotal = float(unit_price_elem[1:]) * qty
 
      assert float(subtotal_text_elem[1:]) == float(unit_price_elem[1:]) * qty, \
           f"Expected: {expect_subtotal}, Actual: {float(subtotal_text_elem[1:])}"
     

finally:
    #driver.quit()
    pass