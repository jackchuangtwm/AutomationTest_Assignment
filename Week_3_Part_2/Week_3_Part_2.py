import service.seleniumService  
from selenium.webdriver.common.by import By

s = service.seleniumService.selectService()

# Open the Chrome browser
# Go to Demo Store (http://demostore.supersqa.com)
url = 'http://demostore.supersqa.com'
s.open_browser(url)

# # Add “Album” to cart and view cart
value = '//h2[text()="Album"]/ancestor::li/a[text()="Add to cart"]'
s.find_element(By.XPATH, value).click()

value = '//h2[text()="Album"]/ancestor::li/a[@title="View cart"]'
s.find_element(By.XPATH, value).click()

# Change the quantity to 2 and update cart in Cart Page
qty = 2
value = '//div[@class="quantity"]/input' 
s.find_element(By.XPATH, value).clear()
s.find_element(By.XPATH, value).send_keys(qty)

value = '//button[@name="update_cart"]'
s.find_element(By.XPATH, value).click()

# Verify that Subtotal is $30.00
# 因為按了update cart，如果直接去判斷價格會出現問題，
# 時間太短了，但為了必免使用wait方式，所以這觀察了一下
# 我們可以等到update cart的alert消失後，再去判斷，
# 因此我們可以判斷 Proceed to checkout是否可以按
# 但在寫W4P1作業的時候，發現了比較好的方式，之後可以參考find_element_unclickable
value = '//div[@class="cart_totals"]/div/a'
s.check_element_click(By.XPATH, value)

value='//td[@data-title="Subtotal"]'
subtotal = s.find_element(By.XPATH, value).text
value='//a[text()="Album"]/ancestor::tr/descendant::span[contains(@class, "amount")]/bdi'
prod_price = s.find_element(By.XPATH, value).text
expect_subtotal = float(prod_price[1:]) * qty

# print(subtotal)
if float(subtotal[1:]) != expect_subtotal:
     print('Subtotal is failed')
else:
     print('success')

# Click “Checkout” and Fill in the form as below:
value = '//div[@class="wc-proceed-to-checkout"]'
s.find_element(By.XPATH, value).click()

# First Name: “First”
value ='//*[@id="billing_first_name"]'
s.find_element(By.XPATH, value).send_keys('First')

# Last Name: “Last”
value ='//*[@id="billing_last_name"]'
s.find_element(By.XPATH, value).send_keys('Last')

# Company: ABC Company
value ='//*[@id="billing_company"]'
s.find_element(By.XPATH, value).send_keys('ABC Company')

# Country / Region: Taiwan
value ='//*[@id="select2-billing_country-container"]'
s.find_element(By.XPATH, value).click()

value ='//input[@class="select2-search__field"]'
s.find_element(By.XPATH, value).send_keys('Taiwan')

value ='//span[@class="select2-results"]/ul/li'
s.find_element(By.XPATH, value).click()

# valueeet address:
value ='//*[@id="billing_address_1"]'
s.find_element(By.XPATH, value).send_keys('Address Line 1')

value ='//*[@id="billing_address_2"]'
s.find_element(By.XPATH, value).send_keys('Address Line 2')

# Town / City: Taipei
value ='//*[@id="billing_city"]'
s.find_element(By.XPATH, value).send_keys('Taipei')

# State / County: Taipei
value ='//*[@id="billing_state"]'
s.find_element(By.XPATH, value).send_keys('Taipei')

# Postcode / ZIP: 101
value ='//*[@id="billing_postcode"]'
s.find_element(By.XPATH, value).send_keys('101')

# Phone: 0123456789
value ='//*[@id="billing_phone"]'
s.find_element(By.XPATH, value).send_keys('0123456789')

# Email: abc@abc.com
value ='//*[@id="billing_email"]'
s.find_element(By.XPATH, value).send_keys('abc@abc.com')

# Create an account with password “1234QWERasdf!@#$” in Checkout Page
value = '//*[@id="createaccount"]'
s.find_element(By.XPATH, value).click()

value = 'account_password'
s.check_element_click(By.ID, value).send_keys('1234QWERasdf!@#$')

# Fill in Additional Information with “Thank you!” in Checkout Page
value ='//*[@id="order_comments"]'
s.find_element(By.XPATH, value).send_keys('Thank you!')
s.find_element(By.XPATH, value).click()

# Click Place Order
value ='//*[@id="place_order"]'
s.find_element(By.XPATH, value).click()

# Verify that “Invalid payment method” is displayed.
value ='//ul[@class="woocommerce-error"]/li'

if s.find_element(By.XPATH, value).text == 'Invalid payment method.':
     print('success, Invalid payment method. is displayed')
else:
     print('Failed')

# Finally, Close the Browser
s.quit_driver()


# Assignment 2 (Advanced Optional)
# Given a list of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):

# # 較耗時，可以用dict的寫法
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []
    
    dict = {}

    for i in range(len(nums)):
        diff = target - nums[i] #計算 target - 陣列中值的差

        if diff in dict: #如果這個差值存在陣列中，回傳結果
                return [dict[diff], i]

        dict[nums[i]] = i


print(two_sum([2, 7, 11, 15], 9)) # Should be [0, 1], because nums[0] + nums[1] = 9
print(two_sum([3, 6, 11, 15], 17)) # Should be [1, 2], because nums[1] + nums[2] = 17
print(two_sum([3, 2, 4], 6))    # Should be [1, 2], because nums[1] + nums[2] = 6
print(two_sum([3, 3, 4], 6))    # Should be [0, 1], because nums[0] + nums[1] = 6
  